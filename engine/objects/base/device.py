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

import paramiko

from typing import List
from time import sleep

from engine.config import USERNAME, PASSWORD, SECRET


class DeviceType:
    SWITCH = 1


class ConnectionType:
    SSH = 1,
    TELNET = 2


class Device:
    __BUFFER__ = 65535
    __DELAY__ = 0.25

    ip_addr: str
    username: str
    password: str
    secret: str
    connection_type: ConnectionType

    def __init__(self, address: str, username: str = USERNAME, password: str = PASSWORD, secret: str = SECRET,
                 conn_type: ConnectionType = ConnectionType.SSH):
        self.ip_addr = address
        self.username = username
        self.password = password
        self.secret = secret
        self.connection_type = conn_type

    def SendConfig(self):
        pass

    def _CliCommand(self, commands: List[str]) -> List[str]:

        pre_conn = paramiko.SSHClient()
        pre_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        pre_conn.connect(str(self.ip_addr),
                         username=self.username,
                         password=self.password,
                         look_for_keys=False,
                         allow_agent=False)
        conn = pre_conn.invoke_shell()
        conn.recv(self.__BUFFER__)

        if commands is not None:
            for command in commands:
                conn.send(command + '\n')

        sleep(self.__DELAY__)
        output = conn.recv(self.__BUFFER__)

        lines = str(output).split("\\r\\n")
        # Popping command and prompt
        lines.pop(0)
        lines.pop(len(lines) - 1)

        pre_conn.close()

        return lines