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

from typing import List

from enum import Enum

from engine.config import USERNAME, PASSWORD, SECRET
from engine.objects.base.device import ConnectionType, Device
from engine.objects.base.interface import InterfaceType, SwitchInterface


class SwitchType(Enum):
    CISCO_IOS = 1


class Switch(Device):
    switch_type: SwitchType

    interfaces: List[SwitchInterface]

    def __init__(self, address: str, username: str = USERNAME, password: str = PASSWORD, secret: str = SECRET,
                 conn_type: ConnectionType = ConnectionType.SSH):
        Device.__init__(self, address, username, password, secret, conn_type)
        self.interfaces = []

    def AddInterface(self, interface: SwitchInterface):
        self.interfaces.append(interface)
        return

    def RemoveInterface(self, intf_type: InterfaceType, intf_number: str):
        for x in self.interfaces:
            if x.interface_type == intf_type and x.interface_number == intf_number:
                self.interfaces.remove(x)

    def __GetInterfaceConfig(self, intf: SwitchInterface) -> List[str]:
        pass