import whois


def getDomainInfo():
    domin=input("Enter Your Domain name : ")
    find=whois.whois(domin)
    print(find)

getDomainInfo()