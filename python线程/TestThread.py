# -*- coding:utf-8 -*-

import threading


class TestThread(threading.Thread):
    def run(self):
        for i in xrange(100):
            print "%s print number:%s" % (self.getName(),i)

for i in range(2):
    t = TestThread()
    t.start()
