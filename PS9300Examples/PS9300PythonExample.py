#
# Copyright (C) 2015-2017 Pico Technology Ltd. See LICENSE file for terms.
#
"""
This is a Python script for controlling a PS9300 sampling ocsilloscope using the PicoSample3 COM object.
This will also work using the demo device in PicoSample3.
"""

import win32com.client
import numpy as np
import matplotlib.pyplot as plt
import time


COMRCW = win32com.client.Dispatch("PicoSample3.COMRC") # create COM object
COMRCW.ExecCommand("Gui:Control:Invisible")

#set up measurements
COMRCW.ExecCommand("Meas:Display:Param")
COMRCW.ExecCommand("Meas:DisplSrc:Ch1")
COMRCW.ExecCommand("Meas:Mode:Single")
COMRCW.ExecCommand("Meas:Ch1:XParam:Freq 1")
COMRCW.ExecCommand("Meas:Ch1:XParam:Rise 1")
COMRCW.ExecCommand("Meas:Ch1:YParam:Max 1")
COMRCW.ExecCommand("Meas:Ch1:YParam:Min 1")
COMRCW.ExecCommand("Meas:Ch1:YParam:PP 1")


COMRCW.ExecCommand("*RunControl:Single")  #set running mode of scope
time.sleep(2)
COMRCW.ExecCommand("Header Off") # turn off headers for returned values

strdata = COMRCW.ExecCommand("Wfm:Data?") #get wfm data for ch1
YU = COMRCW.ExecCommand("Wfm:Preamb:YU?") #get y scale units
XU = COMRCW.ExecCommand("Wfm:Preamb:XU?") #get x scale units
XInc = COMRCW.ExecCommand("Wfm:Preamb:XInc?") #get time sample interval
XOrg = COMRCW.ExecCommand("Wfm:Preamb:XOrg?") #get y axis origin

#Measurements
#List1 = COMRCW.ExecCommand("Meas:Res:List?")
#print(List1)
freq = COMRCW.ExecCommand("Meas:Res:1?")
print("Frequency = " + str(freq))
riseTime = COMRCW.ExecCommand("Meas:Res:2?")
print("Rise Time = " + str(riseTime))
maximum = COMRCW.ExecCommand("Meas:Res:3?")
print("Maximum = " + str(maximum))
minimum = COMRCW.ExecCommand("Meas:Res:4?")
print("Minimum = " + str(minimum))
Pp = COMRCW.ExecCommand("Meas:Res:5?")
print("Peak-to-Peak = " + str(Pp))

#convert data to array of floats
strdata = str(strdata)
strdata = strdata.split(',')
strdata = np.asarray(strdata)
data = strdata.astype(np.float)

#create time data array
totaltime = len(data) * float(XInc)
totaltime = float(totaltime)
datatime = np.linspace(0, totaltime, len(data))

#plot data
plt.plot(datatime, data)
plt.xlabel('Time (' + XU +')')
plt.ylabel('Voltage (' + YU +')')
plt.show()

COMRCW = 1