print("Hello, welcome to NetPulse!")
print("Following Commands will be run on your system - Make sure you have the Internet Connection!!\n")

print("ping : \nipconfig /all : \nhostname : \ngetmac : \narp -a : \ntracert : \nnslookup : \nnetstat -a : \nroute print : \n")

import subprocess
# def ping():
#     a=input("Enter the IP address or domain to ping: ")
#     subprocess.run(["ping", a])
# ping()

# def ipconfig():
#     subprocess.run(["ipconfig", "/all"])
# ipconfig()

# def hostname():
#     subprocess.run(["hostname"])
# hostname()

# def getmac():
#     subprocess.run(["getmac"])
# getmac()

# def arp():
#     subprocess.run(["arp", "-a"])
# arp()

# def tracert():
#     a=input("Enter the IP address or domain to trace: ")
#     subprocess.run(["tracert", a])
# tracert()

# def nslookup():
#     a=input("Enter the IP address or domain to look up: ")
#     subprocess.run(["nslookup", a])
# nslookup()

def netstat():
    subprocess.run(["netstat", "-a"])
netstat()