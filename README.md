# DNS Response Time Tester

A Python-based tool for measuring and analyzing DNS response times across multiple domains. This tool is particularly useful for testing local DNS servers, comparing DNS providers, and monitoring DNS performance.

## Features

- Test DNS response times for multiple domains simultaneously
- Configurable number of queries per domain
- Parallel testing with adjustable thread count
- Comprehensive default domain list (200+ domains)
- Support for custom domain lists
- Detailed statistics including min, max, and average response times
- Summary statistics for overall performance analysis
- Zero external dependencies beyond Python's DNS resolver

## Prerequisites

- Python 3.x
- `dnspython` library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/14wkinnersley/Local-DNS-Test.git
cd dns-response-tester
```

2. Install required packages:
```bash
# Update package list (Ubuntu/Debian)
sudo apt update

# Install Python if not already installed
sudo apt install python3 python3-pip -y

# Install DNS Python library
pip3 install dnspython
```

## Usage

### Basic Usage

```bash
python3 dns_test.py --dns-server YOUR_DNS_SERVER_IP
```

### Advanced Options

```bash
python3 dns_test.py --dns-server YOUR_DNS_SERVER_IP --domains-file domains.txt --queries 5 --threads 10
```

### Command Line Arguments

- `--dns-server`: IP address of the DNS server to test (required)
- `--domains-file`: Path to file containing domains to test (optional)
- `--queries`: Number of queries per domain (default: 3)
- `--threads`: Number of concurrent testing threads (default: 5)

## Domain Lists

### Default Domains
The script includes a comprehensive default list of domains covering various categories:
- Technology & Social Media
- E-commerce & Shopping
- Tech Companies
- Streaming & Entertainment
- Cloud & Infrastructure
- News & Media
- Productivity & Business
- Education & Reference
- Banking & Finance
- CDN & Internet Infrastructure
- Gaming

### Custom Domain List
You can create your own domain list file with one domain per line:
```text
google.com
facebook.com
example.com
```

## Sample Output

```
Testing DNS response times for 192.168.1.13
Testing 200 domains with 3 queries each
----------------------------------------------------------------------
Domain                              Avg (ms)   Min (ms)   Max (ms)   Errors
----------------------------------------------------------------------
cloudflare.com                      2.90       2.11       4.27       0
microsoft.com                       4.64       3.31       5.47       0
google.com                         6.09       2.56       10.44      0
...

Summary:
----------------------------------------------------------------------
Total domains tested: 200
Overall average response time: 15.23 ms
Fastest domain: cloudflare.com (2.90 ms)
Slowest domain: cdn.jsdelivr.net (1805.49 ms)
```

## Files in Repository

- `dns_test.py`: Main script for DNS response time testing
- `domains.txt`: Comprehensive list of domains for testing
- `README.md`: This documentation file

## Use Cases

- Testing local DNS server performance
- Comparing different DNS providers
- Monitoring DNS resolution times
- Troubleshooting DNS issues
- Benchmarking DNS server configurations

## License

This project is licensed under the MIT License

## Acknowledgments

- Uses `dnspython` for DNS resolution
- Domain list curated from various popular and essential internet services
- Inspired by the need for simple, effective DNS testing tools

## Author

Your Name ([@14wkinnersley](https://github.com/14wkinnersley))

## Support

For support, please open an issue in the GitHub repository.
