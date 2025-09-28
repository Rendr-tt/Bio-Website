import subprocess
import os
import socket

onlineIp = []
subnet = "192.168.100."

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return None
    

for i in range(1, 20):
    ip = subnet + str(i)
    try:
        subprocess.check_output(f"ping -n 1 -w 001 {ip} >nul", timeout=0.1, shell=True)
        print(f"Online Device found at: {ip}")
        onlineIp.append(ip)
        

    except subprocess.TimeoutExpired:
        print(f"{ip} is empty")

    except subprocess.CalledProcessError:
        print(f"Error pinging {ip}")

print(onlineIp)

for ip in onlineIp:
    hostname = get_hostname(ip)
    if hostname:
        print(f"{ip} is online - Hostname: {hostname}")
    else:
        print(f"{ip} is online - Hostname: Unknown")



