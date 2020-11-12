###SSH key-management toolkit for multiple hosts by Greedo###
import json
import paramiko
import argparse
import os
import os.path
import sys
from connector import execute_command_readlines

#SSH Config Directories
ssh_dir = "~/.ssh/"
ssh_auth_keys = "~/.ssh/authorized_keys"
ssh_known_hosts = "~/.ssh/known_hosts"

#Set starter values
address=""
port_number=""
command = "ls" 
usr = "tomcat" #Define user for remote host
pwd = "" #Set password for remote hosts

#Json Imports
ports_file = open ('ports.json') #Import port numbers from json
ports_array = json.load(ports_file)

hosts_file = open ('hosts.json') #Import hostnames from json
hosts_array = json.load(hosts_file)

interval = int(len(hosts_array)) #Define interval for main function

#Set options
parser = argparse.ArgumentParser()
parser.add_argument("-list", help="Lists out the authorized_keys by hosts on multiple remote hosts to local .txt file", action="store_true")
parser.add_argument("-add", help="Add public key to authorized_keys on multiple remote hosts", action="store_true")
parser.add_argument("-remove", help="Remove public key from authorized_keys on multiple remote hosts", action="store_true")
#parser.add_argument("-print", help="Prints out authorized keys on specified remote hosts", action="store_true")
args = parser.parse_args()

#Get config file and workdir from User
#current_config = raw_input("Type in the full path of the current config file \n")
workdir = raw_input("Define the local directory where public keys can be verified or asign a stabil value to workdir variable \n")
#workdir = ""
current_key = raw_input("Paste here the public key if you want to Add or Remove or Press Enter to Continue -->  ")


print("Configuration files : " + "\n" + "Hosts : " +  str(hosts_array)  + "\n" + "Ports : " + str(ports_array))

#Create list auth_key function

def list_keys(address, port_number):

	command = "cat ~/.ssh/authorized_keys"
	#Connect via SSH and list
	r_out = execute_command_readlines(address, usr, pwd, command, port_number)	
#Create add key to auth_keys fuction

def add_keys(address, port_number):
	print("Watch out! You are going to modify SSH configuration file [authorized_keys] on multiple servers." + "\n")
	print("Is that OK? Y/N" + "\n")
	isthatok = raw_input("")
	
	if (isthatok == "Y" or isthatok == "Yes" or isthatok == "I" or isthatok == "Igen" or isthatok == "i" or isthatok == "y"):#Check user's answer
		print("OK")

	else:
		print("Aborting . . .")
		sys.exit()

	#Validate the key
	os.popen("echo {0} > {1}/key_valid.pub".format(current_key, workdir))
	validation = os.popen("ssh-keygen -l -f {0}/key_valid.pub && echo done".format(workdir))
	result = validation.read()
	os.popen("rm key_valid.pub")

	#If the key is not valid abort
	if "done" not in result:
		print("This is not a valid SSH public key! \n Aborting . . . ")
		sys.exit()
	else:
		command = "echo {0} >> ~/.ssh/authorized_keys".format(current_key)
		#Connect via SSH and modify or list
		r_out = execute_command_readlines(address, usr, pwd, command, port_number)

def remove_keys(address, port_number):
	print("Watch out! You are going to modify SSH configuration file [authorized_keys] on multiple servers." + "\n")
	print("Is that OK? Y/N" + "\n")
	isthatok = raw_input("")
	
	if (isthatok == "Y" or isthatok == "Yes" or isthatok == "I" or isthatok == "Igen" or isthatok == "i" or isthatok == "y"):#Check user's answer
		print("OK")

	else:
		print("Aborting . . .")
		sys.exit()

	#Validate the key
	#current_key = raw_input("Please type in the removable public SSH key : ")
	os.popen("echo {0} > {1}/key_valid.pub".format(current_key, workdir))
	validation = os.popen("ssh-keygen -l -f {0}/key_valid.pub && echo done".format(workdir))
	result = validation.read()
	os.popen("rm key_valid.pub")

	#If the key is not valid abort
	if "done" not in result:
		print("This is not a valid SSH public key! \n Aborting . . . ")
		sys.exit()
	else:	
		command = "grep -v '{0}' {1} > ~/.ssh/tmp_authorized_keys ".format(current_key, ssh_auth_keys)
		#Connect via SSH and modify or list
		r_out = execute_command_readlines(address, usr, pwd, command, port_number)
		command = "rm ~/.ssh/authorized_keys && mv ~/.ssh/tmp_authorized_keys ~/.ssh/authorized_keys".format(current_key, ssh_auth_keys)
		r_out = execute_command_readlines(address, usr, pwd, command, port_number)
		
def __main__():

	#Call listing function
	if (args.list):
		list_keys(address, port_number)

	#Call add function
	elif (args.add):
		add_keys(address, port_number)

	#Call remove function
	elif(args.remove):
		remove_keys(address, port_number)

#Start the tool!
for i in range(interval):
	address = hosts_array[i-1]
	print("-----------------------------------------------------------------------------------------------------------")
	print(address)
	port_number = int(ports_array[i-1])
	print(port_number)
	__main__()	
	print("-----------------------------------------------------------------------------------------------------------")






























		
		
		
