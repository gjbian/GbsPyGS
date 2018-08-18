# -*- coding:utf-8 -*-
# GodBian

import threading

class MyLogicThread(threading.Thread):
    import mainloop
    g_Mainloop = mainloop

    def __init__(self):
        import cmdhandler
        self.m_CmdHandler = cmdhandler

    def run(self):
        while not MyLogicThread.g_Mainloop.g_bCloseSever:
            self.m_CmdHandler.HandleCmd()
