# -*- coding:utf-8 -*-
# GodBian

import mainlogic
import pubnet

print("MainServerStart...")

g_MainLogicPool = []
g_PubNetOutputPool = []

g_bCloseSever = False

oPubNetThread = pubnet.MyPubNetThread()
oMainLogicThread = mainlogic.MyLogicThread()

lThreadPool = list()
lThreadPool.append(oPubNetThread)
lThreadPool.append(oMainLogicThread)

for oThread in lThreadPool:
    oThread.setDaemon(True)
    oThread.start()

for oThread in lThreadPool:
    oThread.join()

print("MainServerClose...")


