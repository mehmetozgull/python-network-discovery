import scapy.all as scapy
import optparse

# 1- arp_request
# 2- broadcast
# 3- response
# scapy.ls(scapy.ARP())

def getUserInput():
    parseObject = optparse.OptionParser()
    parseObject.add_option("-r", "--range", dest="varOfRange", help="range to scan")
    (userInput, arguments) = parseObject.parse_args()

    if not userInput.varOfRange:
        raise ValueError("Enter the ip address range. (-r *required)")

    return userInput.varOfRange

def netScanner(range):
    arpRequestPacket = scapy.ARP(pdst=range)
    broadcastPacket = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combinedPacket = broadcastPacket / arpRequestPacket
    (answeredList, unansweredList) = scapy.srp(combinedPacket, timeout=1)
    answeredList.summary()

print("===================================================")
range = getUserInput()
ipMacList = netScanner(range)
print("===================================================")