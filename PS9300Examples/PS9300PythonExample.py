#
# Copyright (C) 2018 Pico Technology Ltd. See LICENSE file for terms.
#
"""
This is a Python script for controlling a PicoScope 9300 Series sampling ocsilloscope using the PicoSample3 COM object.
This will also work using the demo device in PicoSample3.
"""

import win32com.client
import numpy as np
import matplotlib.pyplot as plt
import time


COMRCW = win32com.client.Dispatch("PicoSample3.COMRC") # create COM object
COMRCW.ExecCommand("Gui:Control:Invisible")

# Set up measurements
COMRCW.ExecCommand("Meas:Display:Param")
COMRCW.ExecCommand("Meas:DisplSrc:Ch1")
COMRCW.ExecCommand("Meas:Mode:Single")
COMRCW.ExecCommand("Meas:Ch1:XParam:Freq 1")
COMRCW.ExecCommand("Meas:Ch1:XParam:Rise 1")
COMRCW.ExecCommand("Meas:Ch1:YParam:Max 1")
COMRCW.ExecCommand("Meas:Ch1:YParam:Min 1")
COMRCW.ExecCommand("Meas:Ch1:YParam:PP 1")


COMRCW.ExecCommand("*RunControl:Single")  # Set running mode of scope
time.sleep(2)
COMRCW.ExecCommand("Header Off") # Turn off headers for returned values

strdata = COMRCW.ExecCommand("Wfm:Data?")       # Get wfm data for ch1
YU = COMRCW.ExecCommand("Wfm:Preamb:YU?")       # Get y scale units
XU = COMRCW.ExecCommand("Wfm:Preamb:XU?")       # Get x scale units
XInc = COMRCW.ExecCommand("Wfm:Preamb:XInc?")   # Get time sample interval
XOrg = COMRCW.ExecCommand("Wfm:Preamb:XOrg?")   # Get y axis origin

# Measurements
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

# Convert data to array of floats
strdata = str(strdata)
strdata = strdata.split(',')
strdata = np.asarray(strdata)
data = strdata.astype(np.float)

# Create time data array
totaltime = len(data) * float(XInc)
totaltime = float(totaltime)
datatime = np.linspace(0, totaltime, len(data))

# Plot data
plt.plot(datatime, data)
plt.title('PicoScope 9300 Series Example')
plt.xlabel('Time (' + XU +')')
plt.ylabel('Voltage (' + YU +')')
plt.show()

COMRCW = 1