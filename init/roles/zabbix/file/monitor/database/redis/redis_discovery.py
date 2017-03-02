#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import subprocess

json_data = dict(data=list())
net_cmd = "sudo netstat -nlpt|awk '$1 ~ /tcp$/ && /redis-server/{print $4}'"

p = subprocess.Popen(net_cmd, shell=True, stdout=subprocess.PIPE)
net_result = p.stdout.readlines()

for server in net_result:
    dic_content = {
        "{#REDIS_NAME}" : "Redis",
        "{#REDIS_PORT}" : server.split(':')[1].strip(),
        "{#REDIS_IPADDR}" : server.split(':')[0].strip()
    }

    json_data['data'].append(dic_content)

result = json.dumps(json_data,sort_keys=True,indent=4)
print result