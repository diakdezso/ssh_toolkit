import json
import os

print("Hi! You are heading to make a config file for SSH-Toolkit\n")

#Arrays and variables for config

ports_config = "ports.json"
hosts_config = "hosts.json"
host_number = input("Please give me the number of hosts you are going to set in the config!\n")
ports = []
hosts = []

for i in range(host_number):
	host = raw_input("Give me a hostname : " + "\n")
	port = raw_input("Give me the SSH port_number for the previous hostname : y" + "\n")
	hosts.append(host)
	ports.append(port)


with open(ports_config, 'wb') as outfile:
	json.dump(ports, outfile)

with open(hosts_config, 'wb') as outfile:
	json.dump(hosts, outfile)
	
print(ports)
print(hosts)
