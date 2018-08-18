# -*- coding:utf-8 -*-
# GodBian

import mainloop

'''
g_HandleFuncTable = {iSub: oHandleFunc}
'''
g_HandleFuncTable = {

}

def HandleCmd():
    for netCmd in mainloop.g_MainLogicPool:
        iSub = netCmd.UnpackInt(1)
        if iSub in g_HandleFuncTable:
            g_HandleFuncTable[iSub](netCmd)
        else:
            netCmd.PrintAll()
