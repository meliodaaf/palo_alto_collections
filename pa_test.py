#!/usr/bin/env python3

# curl -H "Content-Type: application/x-www-form-urlencoded" -X POST https://firewall/api/?type=keygen -d 'user=<user>&password=<password>'
# <response status = 'success'><result><key>LUFRPT0wczQxMWgxR1BzVmhtVlY0dmxxcnlMbWNnTlk9M0NCZkhWTFhSK3lmaTk4SEc3bXE0V202QkNML2d1dHlHVUhCbHlHLzJ0WT0=</key></result></response>

from panos.firewall import Firewall
import xmltodict

host = "192.168.31.200"
user = "admin"
api_key = "LUFRPT0wczQxMWgxR1BzVmhtVlY0dmxxcnlMbWNnTlk9M0NCZkhWTFhSK3lmaTk4SEc3bXE0V202QkNML2d1dHlHVUhCbHlHLzJ0WT0="
fw = Firewall(hostname=host, user=user, api_key=api_key)

sw_version = fw.get_device_version()
sys_info = fw.op("show system info", xml=True)
xml_data = xmltodict.parse(sys_info)

print(sw_version)
print(xml_data["response"]["result"])