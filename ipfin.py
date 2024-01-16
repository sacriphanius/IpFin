import socket
import subprocess

def get_ip_addresses(url):
    try:
        ipv4_address = socket.gethostbyname(url)
        ipv6_address = socket.getaddrinfo(url, None, socket.AF_INET6)[0][4][0]

        return ipv4_address, ipv6_address
    except socket.gaierror as e:
        return None, None

def get_whois_info(ip_address):
    try:
        whois_info = subprocess.check_output(['whois', ip_address], universal_newlines=True)
        return whois_info
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

if __name__ == "__main__":
    website_url = input("Enter the website URL: ")

    ipv4_address, ipv6_address = get_ip_addresses(website_url)

    if ipv4_address and ipv6_address:
        print(f"\nIPv4 Address: {ipv4_address}")
        print(f"IPv6 Address: {ipv6_address}")

        # IPv4 için WHOIS bilgilerini al
        whois_info_ipv4 = get_whois_info(ipv4_address)
        print("\nWHOIS Information for IPv4:")
        print(whois_info_ipv4)

    elif ipv4_address:
        print(f"\nIPv4 Address: {ipv4_address}")
        print("IPv6 Address not available.")

        # IPv4 için WHOIS bilgilerini al
        whois_info_ipv4 = get_whois_info(ipv4_address)
        print("\nWHOIS Information for IPv4:")
        print(whois_info_ipv4)

    elif ipv6_address:
        print("\nIPv4 Address not available.")
        print(f"IPv6 Address: {ipv6_address}")

    else:
        print("\nUnable to resolve IP addresses for the given website.")
