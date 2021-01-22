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

from jinja2 import Environment, FileSystemLoader

from engine.config import USERNAME, PASSWORD, SECRET
from engine.objects.base.device import ConnectionType
from engine.objects.base.interface import InterfaceType
from engine.objects.base.switch import Switch


class IOSSwitch(Switch):

    def __init__(self, address: str, username: str = USERNAME, password: str = PASSWORD, secret: str = SECRET,
                 conn_type: ConnectionType = ConnectionType.SSH):
        Switch.__init__(self, address, username, password, secret, conn_type)

    def SendConfig(self):
        env = Environment(loader=FileSystemLoader('engine/templates/cisco'))

        template = env.get_template('switch_interface.txt')
        template.globals['InterfaceType'] = InterfaceType

        output = template.render(secret=self.secret, interfaces=self.interfaces)

        result = self._CliCommand(output.splitlines())
