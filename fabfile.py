# -*- coding: utf-8 -*-

import os
from fabric.api import *
from lib.tools import *
from lib.server_init import *

def l(*args):
    #python里面排版好麻烦 T_T
    usage = """
Usage:
    fab l => Show Usage

    fab l:'*' [cmd]
    fab l:'dev-*' [cmd]
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
    pass

def uptime():
    run('uptime')
    pass
