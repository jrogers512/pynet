#!/usr/bin/env python
##Import stuff
import pynetlib, telnetlib

#Define stuff
TELNET_PORT = 23
TELNET_TIMEOUT = 6
ip_addr = '184.105.247.70'
username = 'pyclass'
password = '88newclass'

def main():
    telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    output = remote_conn.read_until('sername ', TELNET_TIMEOUT)
    remote_conn.read_very_eager()
    remote_conn.write('show ip int brief' + '\n')
    remote_conn.close() 

##Only run if not called by another file/program
if __name__ == "__main__":
    main()


