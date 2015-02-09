# -*- coding: utf-8 -*-

from fabric.api import *


def server_tengine(user='webuser', version=None, tornado=True, process=1, connection=1024):
    """
    syslog note
    # need change config use syslog-ng
    # source s_sys {
    #         file ("/proc/kmsg" program_override("kernel: "));
    #         unix-dgram ("/dev/log");
    #         internal();
    #         udp(ip(0.0.0.0) port(514));
    #     };

    # gd-progs use for image-fliter

    :param version:
    :param user:
    :param tornado:
    :return:
    """

    utils_baselib()
    run('yum install jemalloc jemalloc-devel  -y')
    run('yum install GeoIP GeoIP-devel GeoIP-update GeoIP-update6 -y')
    run('yum install pcre-devel openssl-devel nginx -y')

    run('chkconfig --level 35 nginx off')

    if version:
        run('wget http://tengine.taobao.org/download/tengine-{0}.tar.gz -O /tmp/tengine-{0}.tar.gz'.format(version))
    else:
        cmd_git('/tmp/tengine', 'https://github.com/nextoa/tengine.git')

    io_slowlog('nginx', user=user)
    io_aircache('nginx', size=1)

    run('test -d /usr/local/var/lock || mkdir -p /usr/local/var/lock')

    with cd('/tmp'):

        if version:
            run('tar -xvzpf tengine-{0}.tar.gz'.format(version))

        real_path = '/tmp/tengine-{0}'.format(version) if version else '/tmp/tengine'

        with cd(real_path):
            # --without-http_uwsgi_module
            run('./configure --prefix=/usr/local --user={0} --group={0} --conf-path=/etc/nginx  --sbin-path=/usr/local/sbin '
                ' --without-http_scgi_module --without-http_memcached_module --without-http_autoindex_module '
                ' --without-http_auth_basic_module'
                ' --with-http_spdy_module'
                ' --with-jemalloc --with-http_spdy_module'
                ' --with-http_realip_module'
                ' --with-http_concat_module '

                # dir path
                '--pid-path=/usr/local/var/run/nginx.pid --lock-path=/usr/local/var/lock/nginx '

                # file path
                ' --http-client-body-temp-path=/aircache/nginx/body_temp'
                ' --http-proxy-temp-path=/aircache/nginx/proxy_temp'
                ' --error-log-path=/logs/nginx/error.log --http-log-path=/logs/nginx/access.log'
                ' --with-syslog'
                # ' --with-http_reqstat_module'
                ' --with-http_stub_status_module'
                ' --with-http_geoip_module'

                ' --with-http_gzip_static_module'
                ' --with-http_ssl_module'
                ' --with-pcre'
                ' --with-file-aio'

                # ' --with-http_upstream_keepalive_module'

                ' --with-http_ssl_module '
                ' --with-http_footer_filter_module=shared'
                ' --with-http_sysguard_module=shared'
                ' --with-http_addition_module=shared'
                # ' --with-http_xslt_module=shared'
                # ' --with-http_image_filter_module=shared'
                # ' --with-http_rewrite_module=shared '
                ' --with-http_sub_module=shared'
                ' --with-http_flv_module=shared'
                ' --with-http_slice_module=shared'
                ' --with-http_mp4_module=shared'
                ' --with-http_random_index_module=shared'
                ' --with-http_secure_link_module=shared'
                ' --with-http_sysguard_module=shared'
                ' --with-http_charset_filter_module=shared'
                ' --with-http_userid_filter_module=shared'


                ' --with-http_footer_filter_module=shared'.format(user))

            run('make')

            with settings(warn_only=True):
                run('service tengine stop')

            run('make install')

            pass

    try:
        template = pkg_resources.resource_string('fabez', 'tpl/nginx.conf')
    except:
        template = open(os.path.join(os.path.dirname(__file__), 'tpl', 'nginx.conf')).read()
        pass

    buf = template.replace('{$user}', user) \
        .replace('{$process}', str(process)) \
        .replace('{$connection}', str(connection))

    # only support python2.x
    with tempfile.NamedTemporaryFile('w', delete=False) as fh:
        print>> fh, buf

    put(fh.name, '/etc/nginx/nginx.conf')

    os.remove(fh.name)

    try:
        template = pkg_resources.resource_string('fabez', 'tpl/nginx.start')
    except:
        template = open(os.path.join(os.path.dirname(__file__), 'tpl', 'nginx.start')).read()
        pass

    buf = template

    # only support python2.x
    with tempfile.NamedTemporaryFile('w', delete=False) as fh:
        print>> fh, buf

    put(fh.name, '/etc/init.d/tengine')

    os.remove(fh.name)

    try:
        template = pkg_resources.resource_string('fabez', 'tpl/nginx.sysconfig')
    except:
        template = open(os.path.join(os.path.dirname(__file__), 'tpl', 'nginx.sysconfig')).read()
        pass

    buf = template

    # only support python2.x
    with tempfile.NamedTemporaryFile('w', delete=False) as fh:
        print>> fh, buf

    put(fh.name, '/etc/sysconfig/nginx')

    os.remove(fh.name)

    run('chmod +x  /etc/init.d/tengine')
    run('chkconfig --level 35 tengine on')
    pass

