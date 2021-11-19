#!/usr/local/bin/python3

import json
import subprocess

def mbps(speed):
    return int(round((speed / 1024 / 1024), 0))

# Args: c – outputs in JSON, s – tests download and upload separately
cmd = ["/usr/bin/networkQuality", "-c", "-s"]

response = json.loads(
    subprocess.run(cmd, capture_output=True, text=True).stdout
)

# Download Speed in Mbps
dl_throughput = mbps(response.get("dl_throughput", 0))

# Upload Speed in Mbps (not used at the moment)
# ul_throughput = mbps(response.get("ul_throughput", 0))

print(dl_throughput)
