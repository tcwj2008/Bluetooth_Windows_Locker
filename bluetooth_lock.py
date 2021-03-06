import bluetooth
import ctypes

"""
To use this tool change the your_device_bluetooth_name to
your device blueooth name - you should be able to find this
in your device's bluetooth settings.
You MUST first pair your device for this to work.

Requirements:
 1. Install PyBluez - https://pypi.python.org/pypi/PyBluez
"""
#--------------Change Here--------------
your_device_bluetooth_name = "Galaxy S6 edge+"
#---------------------------------------


nearby_devices = []
lock = True
try:
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names = True, flush_cache=True, lookup_class=False)
except:
    print "Issue with bluetooth lookup, halting"

for bdaddr, device_name in nearby_devices:
    print device_name, bdaddr #<--for debugging
    services = bluetooth.find_service(address=bdaddr)
    if your_device_bluetooth_name == device_name and len(services)>0:
        print "found",your_device_bluetooth_name,"with address", bdaddr
        lock = False
        break

if lock:
    print "Locking computer!"
    ctypes.windll.user32.LockWorkStation()
