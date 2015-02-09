# -*- coding: utf-8 -*-

from fabric.api import *


def server_nscd():
    yum_install('nscd')
    run('chkconfig --level 35 nscd on')
    run('service nscd start')
    pass




def utils_baselib():
    '''
    install base package
    :return:
    '''
    run('yum install gcc-c++ make zlib-devel libxml2  libxml2-devel  bzip2-libs bzip2-devel  libcurl-devel  libjpeg libjpeg-devel  libpng libpng-devel  freetype freetype-devel  libmcrypt libmcrypt-devel  libtool-ltdl libtool-ltdl-devel openssl-devel autoconf re2c bison pcre_devel pcre   libtiff-devel libjpeg-devel libzip-devel freetype-devel lcms2-devel libwebp-devel tcl-devel tk-devel -y')
    pass



def utils_imagelib():
    run('yum install libtiff-devel libjpeg-devel libzip-devel freetype-devel  lcms2-devel libwebp-devel tcl-devel tk-devel -y')
    pass


def utils_disktools():
    run('yum install parted xfsprogs kmod-xfs -y')
    pass



def utils_epel():
    """
    install epel lib
    :return:
    """
    with settings(warn_only=True):
        run('rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm')
    pass

