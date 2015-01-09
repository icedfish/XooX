# -*- coding: utf-8 -*-

import os
from fabric.api import *
from lib.xoox import *
from lib.all import *

#avoid local known_host changes
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


def init_centos_6():
    "Designed for init CentOS 6.6 x64"
    #yum upgrade
    #tsar
    #service
    #dns + nscd
    #ulimit
    #disable ipv6
    #bash improve
    pass

@parallel(pool_size=5)
def uptime():
    run('uptime')
    pass
