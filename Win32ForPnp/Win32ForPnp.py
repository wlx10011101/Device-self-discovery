# coding=utf-8
'''
Created on 20170216

@author: WLX
'''

import wmi

class Win32ForPnp(object):


    def __init__(self):
        pass
    
    def getPnpDeviceInfo(self):
        i = 0
        windows = wmi.WMI()
        wql = "SELECT * FROM Win32_PnPEntity WHERE Manufacturer != 'Microsoft' AND NOT PNPDeviceID LIKE 'ROOT\\%'"
        print ("All physical PNP devices")
        for J in windows.query(wql):
            print "{0}>>>>:".format(i)
            print(J)
            i += 1
#             
if __name__ == "__main__":
    print ">>>>"
    import sys
    reload(sys)
    sysEnoding = sys.getdefaultencoding()
    if sysEnoding is not 'utf-8':
        sys.setdefaultencoding('utf-8')
        
    Win32ForPnp().getPnpDeviceInfo()
    print "<<<<"