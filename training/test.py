import subprocess
import socket
import platform

def ping(ip):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', ip]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return None

def scan_network(base_ip):
    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        if ping(ip):
            hostname = get_hostname(ip)
            if hostname:
                print(f"{ip} is online - Hostname: {hostname}")
            else:
                print(f"{ip} is online - Hostname: Unknown")

if __name__ == "__main__":
    base_ip = input("Enter the first three octets of your subnet (e.g. 192.168.1): ")
    scan_network(base_ip)

