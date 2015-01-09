# -*- coding: utf-8 -*-

import glob
from fabric.contrib.console import confirm
from fabric.utils import abort

def parse_hosts(str):
	list = []
	for _file in glob.glob('./server_list/' + str + '.conf'):
		fo = open(_file, 'r')
		while True :
			_line = fo.readline().strip()
			if not _line:
				break
			list.append(_line)
	if str != '*' or confirm("Are you sure about running on *** ALL SERVERS *** ?") :
		return list
	else :
		abort("Aborting at user request.")
