# MAC Address Changer Script
# ctrl + / comments all highlighted lines
import subprocess


interface = input("enter interface: ") # for python2
new_mac = input("enter new mac: ") # do "raw_input" instead of "input"
print("[+] Changing MAC Address for: " + interface + " to: " + new_mac)

subprocess.call("ifconfig " + interface, shell=True) #see old mac
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
subprocess.call("ifconfig " + interface, shell=True) #see changed mac
print(new_mac)
# ctrl + d pastes line below
# changes mac adress to 00:11:22:33:44:66
# subprocess is a library that lets you run OS commands
