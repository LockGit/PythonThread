# -*- encoding:utf-8 -*-
#/usr/bin/python env
#Author:Lock.Esc
from time import ctime,sleep
import threading
import sys

def music(name):
	print('listen to music:'+name+' now is '+ctime())
	sleep(1)

def movie(name):
	print('watch movie :'+name+' now is '+ctime())
	sleep(3)

if __name__ == '__main__':
	# music('My Music') # listen to music:My Music now is Mon Jan 11 00:49:36 2016
	# movie('My Movie') # watch movie :My Movie now is Mon Jan 11 00:49:37 2016
	# print('all done:'+ctime()) # all done:Mon Jan 11 00:49:40 2016
	
	# 多线程
	threadlist = []
	t1 = threading.Thread(target=music,args=('My Music',))
	threadlist.append(t1)
	t2 = threading.Thread(target=movie,args=('My Movice',))
	threadlist.append(t2)
	for t in threadlist:
		t.setDaemon(True)
		t.start()
	# for t in threadlist:
	# 	t.join()
	print('all done:'+ctime())

	# listen to music:My Music now is Mon Jan 11 01:07:42 2016
	# watch movie :My Movice now is Mon Jan 11 01:07:42 2016
 	# all done:Mon Jan 11 01:07:42 2016