# PythonThread
Python Version  Thread Test


join() 与 setDaemon 的区别
------------
join([timeout])
    主线程A中调用了B.join()，那么，主线程A会在调用的地方等待，直到子线程B完成操作后，才可以接着往下执行，那么在调用这个线程时可以使用被调用线程的join方法，里面的参数时可选的，代表线程运行的最大时间，即如果超过这个时间，不管这个此线程有没有执行完毕都会被回收，然后主线程或函数都会接着执行的。

setDaemon设置守护
  主线程A中，创建了子线程B，并且在主线程A中调用了B.setDaemon(),这个的意思是，把主线程A设置为守护线程，这时候，要是主线程A执行结束了，就不管子线程B是否完成,一并和主线程A退出.这就是setDaemon方法的含义，这基本和join是相反的。
  

threading.Thread(target=movie,args=('My Movice',))
   args中最后加了一个逗号，这个逗号加上之后，程序执行就可以看到线程中的print信息。
