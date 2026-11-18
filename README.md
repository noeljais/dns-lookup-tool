
# DNS Lookup Tool

A simple Python command-line tool that resolves domain names into IPv4 and IPv6 addresses.

## Features

- Accepts a domain name from the user
- Retrieves IPv4 and IPv6 addresses using DNS resolution
- Displays IPv4 and IPv6 addresses separately
- Removes duplicate IP addresses
- Sorts the results for easier reading
- Handles DNS lookup errors

## Technologies Used

- Python 3
- socket module
- ipaddress module

## How to Run

1. Install Python 3.
2. Clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python dns_lookup.py
```

5. Enter a domain name such as `google.com`.

## Example Output

```text
Enter a domain name: cloudflare.com

Domain: cloudflare.com

IPv4 Addresses:
104.16.132.229
104.16.133.229

IPv6 Addresses:
No IPv6 addresses found.
```

The addresses returned depend on the system's DNS resolver and network configuration.

## How It Works

The program uses Python's `socket.getaddrinfo()` function to resolve a domain name into network address information. It extracts the IP addresses, identifies whether each address is IPv4 or IPv6, and stores them in separate sets to remove duplicates.

Finally, it displays the unique addresses and handles DNS resolution errors.

## Learning Outcomes

- Understanding DNS and domain name resolution
- Understanding IPv4 and IPv6 addressing
- Using Python's socket and ipaddress modules
- Working with sets and loops
- Handling exceptions in Python

## Limitations

- Results depend on the system's DNS resolver.
- Not all IPv4 or IPv6 addresses associated with a domain are guaranteed to be returned.
- Does not retrieve MX, NS, TXT, or other DNS record types.

## Future Improvements

- Support for additional DNS record types
- Option to choose a DNS server
- Exporting results to a text or CSV file
