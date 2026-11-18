import socket
import ipaddress

try:
    domain = input("Enter a domain name: ").strip()
    result = socket.getaddrinfo(domain, None)

    ipv4 = set()
    ipv6 = set()

    for item in result:
        ip = item[4][0]

        if ipaddress.ip_address(ip).version == 4:
            ipv4.add(ip)
        else:
            ipv6.add(ip)

    print("\nDomain:", domain)

    print("\nIPv4 Addresses:")
    for ip in sorted(ipv4):
        print(ip)

    print("\nIPv6 Addresses:")
    for ip in sorted(ipv6):
        print(ip)

    if not ipv4:
        print("No IPv4 addresses found.")

    if not ipv6:
        print("No IPv6 addresses found.")

except socket.gaierror as error:
    print("DNS lookup failed:", error)

except ValueError:
    print("Invalid IP address returned.")
