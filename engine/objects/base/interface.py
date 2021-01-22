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
from enum import Enum


class InterfaceType(Enum):
    PHYSICAL = 1,
    PORTCHANNEL = 2,


class SwitchInterface:
    interface_type: InterfaceType
    interface_number: str

    shutdown: bool
    access_vlan: int
    access_port: bool
    mtu: int

    def __init__(self, intf_number: str):
        if "/" in intf_number:
            self.interface_type = InterfaceType.PHYSICAL
        else:
            self.interface_type = InterfaceType.PORTCHANNEL

        self.shutdown = True
        self.access_vlan = 0
        self.interface_number = intf_number
        self.access_port = True
        self.mtu = 1500

