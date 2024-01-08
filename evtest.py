#!/usr/bin/python
import evdev
from time import sleep

import sys
import redis
r = redis.Redis(host="localhost", password = "", decode_responses=True)
# returns path of gpio ir receiver device
def get_ir_device():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if (device.name == "meson-ir"):
            print("Using device", device.path, "\n")
            return device

    print("No device found!")
    sys.exit()

# returns a generator object that yields InputEvent instances
# raises BlockingIOError if no events available, which much be caught
def get_all_events(dev):
    return dev.read()

# returns the most recent InputEvent instance
# returns NoneType if no events available
def get_last_event(dev):
    try:
        for event in dev.read():	# iterate through all queued events
            if (event.value > 0):
                last_event = event
    except BlockingIOError: # no events to be read
        last_event = None

    return last_event

# returns the next InputEvent instance
# blocks until event is available
def get_next_event(dev):
    while(True):
    	event = dev.read_one()
    	if (event):
    		return event
device = get_ir_device()
def main():
    
    switch = ""
    #print("Waiting 5 seconds for IR signals.  A list of all received commands will be returned.")
    sleep(1)
    events = get_all_events(device)
    try:
        event_list = [event.value for event in events]
        print(event_list)
        for value in event_list:
          if value == 341:
             switch = "on"
             #print("sw True")
          elif value == 320:
             switch = "off"
             #print("sw False")
 

    except BlockingIOError:
        switch = ""
        #print("No commands received.\n")
    return switch
#    print("Waiting 5 seconds for IR signals.  The last received command will be returned.")
#    sleep(5)
#    last_event = get_last_event(device)
#    if last_event is not None:
#        print("Received command:", last_event.value, "\n")
#    else:
#        print("No commands received.\n")

#    print("Waiting indefinitely for IR signals.  The first received command will be returned.")
#    next_event = get_next_event(device)
#    print("Received command:", next_event.value, "\n")

#if __name__ == "__main__":
while True: 
    sleep(0.1)
    ir = main()
    #print(ir)
    if ir == "on":
       r.set("switch", "on")
       print("SWITCH TRUE")
    elif ir == "off":
       r.set("switch", "off")
       print("SWITCH FALSE")
