#
#	Copyright (c) 2020 Cisco and/or its affiliates.
#
#	This software is licensed to you under the terms of the Cisco Sample
#	Code License, Version 1.1 (the "License"). You may obtain a copy of the
#	License at
#
#		       https://developer.cisco.com/docs/licenses
#
#	All use of the material herein must be in accordance with the terms of
#	the License. All rights not expressly granted by the License are
#	reserved. Unless required by applicable law or agreed to separately in
#	writing, software distributed under the License is distributed on an "AS
#	IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#	or implied.
#
from engine.objects.base.device import DeviceType
from engine.objects.base.interface import SwitchInterface, InterfaceType
from engine.objects.base.switch import SwitchType
from engine.objects.cisco.ios_switch import IOSSwitch
from hosts import HOSTS

switches = []

for x in HOSTS:
    if x["type"] == DeviceType.SWITCH:
        if x["subtype"] == SwitchType.CISCO_IOS:
            switches.append(IOSSwitch(x["address"]))
# switch.AddInterface(SwitchInterface(InterfaceType.SVI, "10", "11"))
# switch.AddInterface(SwitchInterface(InterfaceType.PORTCHANNEL, "20", "21"))
# switch.AddInterface(SwitchInterface(InterfaceType.PHYSICAL, "1/30", "1/40"))
# switch.AddInterface(SwitchInterface(InterfaceType.SVI, "40"))
# switch.AddInterface(SwitchInterface(InterfaceType.PORTCHANNEL, "50"))
# switch.AddInterface(SwitchInterface(InterfaceType.PHYSICAL, "2/30"))

intf = SwitchInterface(InterfaceType.PHYSICAL, "0/1")
intf.access_port = True
intf.access_vlan = 20
intf.shutdown = False

for x in switches:
    x.AddInterface(intf)
    x.SendConfig()
