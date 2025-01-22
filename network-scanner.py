import scapy.all as scapy
import argparse

#prompt user for ip range
def get_user_input():
    parser = argparse.ArgumentParser(description="Network Scanner - Provide an IP range to scan.")
    parser.add_argument("-t","--target","-target",
                        dest="target",
                        required = True,
                        help = "Use -t OR --target to define ip Range. Example: 192.x.x.x/24 OR 10 .x.x.x/24"
                        )
    options = parser.parse_args()
    return options.target #Extract the target IP range directly

def scan(ip):
    # Create ARP request
    arp_request = scapy.ARP(pdst=ip)
    # Ethernet frame to broadcast the ARP
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine the two
    arp_request_broadcast = broadcast / arp_request
    # Send request and receive response
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    # Create a list-dictionary to hold each element
    client_list = []
    for element in answered_list:
        client_dictionary = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dictionary)
    return client_list

def print_result(results_list):
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

# Main function
if __name__ == "__main__":
    target_ip = get_user_input()
    scan_result = scan(target_ip)
    print_result(scan_result)
