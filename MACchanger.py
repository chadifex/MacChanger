# MAC Address Changer Script
# ctrl + / comments all highlighted lines
import subprocess # w library
import optparse

def get_arguments():
    parser = optparse.OptionParser()  # object to handle CLI args
    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface to change it's MAC Address")  # dest = where value goes
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")  # dest = destinaton variable
    (options, arguments) = parser.parse_args()  # passes all add_option to function where called
    if not options.interface: #both these check if person put arguments in
        parser.error("[-] Please Specify An Interface to use --help for more info.") #parser.error displays message then exits program
    elif not options.new_mac:
        parser.error("[-] Please Specify A New MAC Address to use --help for more info.")
    return options
    # options contains input, arguments contains --interface, --mac etc

def change_mac(interface, new_mac):
    print("[+] Changing MAC Address for: " + interface + " to: " + new_mac)
    subprocess.call(["ifconfig", interface])  # see old mac
    subprocess.call(["ifconfig", interface, "down"])  # no + but , instead
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface + "up"])  # no space between "" as not using shell=True does it auto
    subprocess.call(["ifconfig", interface])  # see changed mac
    print(new_mac)  # extra verification

# interface = options.interface
# new_mac = options.new_mac
options = get_arguments()
change_mac(options.interface, options.new_mac)

# ctrl + d pastes line below
# changes mac address to 00:11:22:33:44:66
# subprocess is a library that lets you run OS commands
