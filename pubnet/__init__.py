# -*- coding:utf-8 -*-
# GodBian

import threading

class MyPubNetThread(threading.Thread):
    import mainloop
    g_Mainloop = mainloop

    def __init__(self):
        pass

    def run(self):
        while not MyPubNetThread.g_Mainloop.g_bCloseSever:
            pass

