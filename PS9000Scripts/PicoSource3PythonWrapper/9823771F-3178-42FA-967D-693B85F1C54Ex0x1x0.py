# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 2.7.14 |Anaconda, Inc.| (default, Nov  8 2017, 13:40:13) [MSC v.1500 32 bit (Intel)]
# From type library 'PicoSample3.exe'
# On Fri May 25 08:51:19 2018
'PicoSample 3 Type Library'
makepy_version = '0.5.01'
python_version = 0x2070ef0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{9823771F-3178-42FA-967D-693B85F1C54E}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class ICOMRC(DispatchBaseClass):
	'Dispatch interface for PicoSample 3 COMRC Object'
	CLSID = IID('{60BF5C25-86EE-4286-B114-7119DBF2EC20}')
	coclass_clsid = IID('{AE169BF4-11DD-4696-9D29-5B5270BEF4AF}')

	def ExecCommand(self, Command=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(201, LCID, 1, (8, 0), ((8, 1),),Command
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'PicoSample3.COMRC'
class COMRC(CoClassBaseClass): # A CoClass
	# PicoSample 3 COMRC Object
	CLSID = IID('{AE169BF4-11DD-4696-9D29-5B5270BEF4AF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ICOMRC,
	]
	default_interface = ICOMRC

ICOMRC_vtables_dispatch_ = 1
ICOMRC_vtables_ = [
	(( u'ExecCommand' , u'Command' , u'Respond' , ), 201, (201, (), [ (8, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 28 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{AE169BF4-11DD-4696-9D29-5B5270BEF4AF}' : COMRC,
	'{60BF5C25-86EE-4286-B114-7119DBF2EC20}' : ICOMRC,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{60BF5C25-86EE-4286-B114-7119DBF2EC20}' : 'ICOMRC',
}


NamesToIIDMap = {
	'ICOMRC' : '{60BF5C25-86EE-4286-B114-7119DBF2EC20}',
}


