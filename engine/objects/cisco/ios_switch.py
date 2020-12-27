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
from jinja2 import Environment, FileSystemLoader

from engine.config import USERNAME, PASSWORD, SECRET
from engine.objects.base.device import ConnectionType
from engine.objects.base.interface import SwitchInterface, InterfaceType
from engine.objects.base.switch import Switch


class IOSSwitch(Switch):

    __physical_intf_types__ = ("Ethernet", "FastEthernet", "GigabitEthernet", "TenGigabitEthernet")

    def __init__(self, address: str, username: str = USERNAME, password: str = PASSWORD, secret: str = SECRET,
                 conn_type: ConnectionType = ConnectionType.SSH):
        Switch.__init__(self, address, username, password, secret, conn_type)

    def __GetInterfaceConfig(self, intf: SwitchInterface) -> List[str]:
        result = []

        """Compile inner body of interface configuration into a string"""
        config = ["switchport"]
        if intf.access_port:
            config.append("switchport mode access")
            config.append(f"switchport access vlan {intf.access_vlan}")
        else:
            config.append("switchport mode trunk")
            config.append(f"switchport trunk native vlan {intf.access_vlan}")

        if intf.shutdown:
            config.append("shutdown")
        else:
            config.append("no shutdown")

        if intf.interface_end is None:
            """Generate possible interface definitions for a single interface"""
            if intf.interface_type == InterfaceType.SVI:
                result.append(f"interface vlan {intf.interface_start}")
                result.extend(config)
            elif intf.interface_type == InterfaceType.PORTCHANNEL:
                result.append(f"interface portchannel {intf.interface_start}")
                result.extend(config)
            elif intf.interface_type == InterfaceType.PHYSICAL:
                for x in self.__physical_intf_types__:
                    result.append(f"interface {x} {intf.interface_start}")
                    result.extend(config)
        else:
            """Generate possible interface definitions for a range"""
            if intf.interface_type == InterfaceType.SVI:
                result.append(f"interface range vlan {intf.interface_start} - {intf.interface_end}")
                result.extend(config)
            elif intf.interface_type == InterfaceType.PORTCHANNEL:
                result.append(f"interface range portchannel {intf.interface_start} - {intf.interface_end}")
                result.extend(config)
            elif intf.interface_type == InterfaceType.PHYSICAL:
                for x in self.__physical_intf_types__:
                    result.append(f"interface range {x} {intf.interface_start} - {intf.interface_end}")
                    result.extend(config)

        return result

    def SendConfig(self):
        env = Environment(loader=FileSystemLoader('engine/templates/cisco'))

        template = env.get_template('switch_interface.txt')

        output = template.render(secret="cisco", interfaces=self.interfaces)

        result = self._CliCommand(output.splitlines())

        for x in result:
            print(x)
