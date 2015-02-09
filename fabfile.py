# -*- coding: utf-8 -*-

import os
from fabric.api import *
from lib.xoox import *

#avoid local known_hosts changes
env.disable_known_hosts=True

def l(*args):
    #python里面排版好麻烦 T_T
    usage = """
Usage:
    fab l => Show Usage

    fab l:'*' [cmd]
    fab l:'dev-*' [cmd]
    fab l:'*-db-*' [cmd]
    fab l:sample-db [cmd]

Available Commands:"""

    if len(args) == 0  or args[0] == '':
        print usage 
        os.system("grep '^def ' fabfile.py | grep -v ' l(' | sed 's/^def/   /g' | sed 's/\://g'" )
    else :
        env.hosts = parse_hosts(args[0])
        print "Server List: ", env.hosts
        pass
    pass



###########################################
##   以下代码都非必须，可以根据你的实际需要改写 ##
###########################################
from lib.all import *

def init_centos_6():
    "Designed for init CentOS 6.6 x64"
    #yum upgrade
    #tsar
    #service
    #dns + nscd
    #ulimit
    #disable ipv6
    #bash improve

    run('yum install wget -y')

    server_nscd()
    cmd_ulimit()
    utils_epel()

    utils_git()

    io_webdata(uid=user, gid=user)

    io_slowlog('nginx', user)
    # server_nginx(user)
    server_tengine(user=user)

    # io_slowlog('supervisor', user)
    # server_supervisor()

    server_monit()

    pass

##############
## Commands ##
##############

def restart_tengine():
    run('service tengine stop')
    run('service tengine start')
    pass

def restart_monit(config=None):

    if config:
        config_monit(config)
        run('service monit restart')

    pass


def reboot_monit(name=None, config=None):
    if config:
        config_monit(config)
        run('service monit restart')

    if name:
        run('monit restart {}'.format(name))
    # run('service monit restart')
    pass

@parallel(pool_size=5)
def uptime():
    run('uptime')
    pass
