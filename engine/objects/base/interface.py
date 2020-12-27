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

from engine.objects.base.aux import ReturnCode
from engine.objects.base.aux import ConfigurationItem


class InterfaceType:
    PHYSICAL = 1,
    PORTCHANNEL = 2,
    SVI = 3


class SwitchInterface(ConfigurationItem):
    interface_type: InterfaceType
    interface_start: str
    interface_end: str

    shutdown: bool
    access_vlan: int
    access_port: bool

    def __init__(self, intf_type: InterfaceType, intf_start: str, intf_end: str = None):
        self.interface_type = intf_type
        self.shutdown = True
        self.access_vlan = 0
        self.interface_start = intf_start
        self.interface_end = intf_end
        self.access_port = True

    def SetShutdown(self, shutdown: bool) -> None:
        self.shutdown = shutdown

    def SetAccessVlan(self, access_vlan: int) -> None:
        self.access_vlan = access_vlan

    def SetAccessPort(self, access_port: bool) -> None:
        self.access_port = access_port

