#!/usr/bin/env python3
import dns.resolver
import time
import statistics
import argparse
from concurrent.futures import ThreadPoolExecutor

def test_dns_query(domain, dns_server, record_type='A', num_queries=3):
    """
    Test DNS response time for a specific domain
    """
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [dns_server]
    resolver.timeout = 5
    resolver.lifetime = 5
    
    response_times = []
    errors = 0
    
    for _ in range(num_queries):
        try:
            start_time = time.time()
            resolver.resolve(domain, record_type)
            end_time = time.time()
            response_times.append((end_time - start_time) * 1000)  # Convert to milliseconds
        except Exception as e:
            errors += 1
    
    if response_times:
        return {
            'domain': domain,
            'min': min(response_times),
            'max': max(response_times),
            'avg': statistics.mean(response_times),
            'median': statistics.median(response_times),
            'errors': errors
        }
    return None

def main():
    parser = argparse.ArgumentParser(description='DNS Response Time Tester')
    parser.add_argument('--dns-server', required=True, help='DNS server IP address')
    parser.add_argument('--domains-file', help='File containing domains to test (one per line)')
    parser.add_argument('--queries', type=int, default=3, help='Number of queries per domain')
    parser.add_argument('--threads', type=int, default=5, help='Number of concurrent threads')
    args = parser.parse_args()

    # Expanded list of domains covering various categories
    default_domains = [
        # Popular Tech & Social Media
        'google.com',
        'facebook.com',
        'youtube.com',
        'twitter.com',
        'instagram.com',
        'linkedin.com',
        'reddit.com',
        'tiktok.com',
        'pinterest.com',
        'discord.com',
        
        # E-commerce & Shopping
        'amazon.com',
        'ebay.com',
        'walmart.com',
        'etsy.com',
        'shopify.com',
        'aliexpress.com',
        
        # Tech Companies
        'microsoft.com',
        'apple.com',
        'intel.com',
        'amd.com',
        'nvidia.com',
        'oracle.com',
        'ibm.com',
        'cisco.com',
        'dell.com',
        
        # Streaming & Entertainment
        'netflix.com',
        'disney.com',
        'spotify.com',
        'twitch.tv',
        'hulu.com',
        'hbomax.com',
        
        # Cloud & Infrastructure
        'aws.amazon.com',
        'cloud.google.com',
        'azure.microsoft.com',
        'cloudflare.com',
        'digitalocean.com',
        'github.com',
        'gitlab.com',
        
        # News & Media
        'cnn.com',
        'bbc.com',
        'nytimes.com',
        'reuters.com',
        'bloomberg.com',
        
        # Productivity & Business
        'office.com',
        'slack.com',
        'zoom.us',
        'dropbox.com',
        'salesforce.com',
        
        # Education & Reference
        'wikipedia.org',
        'stackoverflow.com',
        'udemy.com',
        'coursera.org',
        'edx.org',
        
        # Banking & Finance
        'paypal.com',
        'chase.com',
        'wellsfargo.com',
        'bankofamerica.com',
        
        # CDN & Internet Infrastructure
        'akamai.com',
        'fastly.com',
        'cdn.jsdelivr.net',
        'unpkg.com'
    ]

    # Read domains from file if provided
    if args.domains_file:
        with open(args.domains_file, 'r') as f:
            domains = [line.strip() for line in f if line.strip()]
    else:
        domains = default_domains

    print(f"\nTesting DNS response times for {args.dns_server}")
    print(f"Testing {len(domains)} domains with {args.queries} queries each")
    print("-" * 70)

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = [
            executor.submit(test_dns_query, domain, args.dns_server, 'A', args.queries)
            for domain in domains
        ]
        
        results = []
        for future in futures:
            result = future.result()
            if result:
                results.append(result)

    # Sort results by average response time
    results.sort(key=lambda x: x['avg'])

    # Print results in a table format
    print(f"{'Domain':<35} {'Avg (ms)':<10} {'Min (ms)':<10} {'Max (ms)':<10} {'Errors':<8}")
    print("-" * 75)
    
    total_avg = 0
    total_domains = len(results)
    
    for result in results:
        print(f"{result['domain']:<35} {result['avg']:<10.2f} {result['min']:<10.2f} "
              f"{result['max']:<10.2f} {result['errors']:<8}")
        total_avg += result['avg']
    
    # Print summary statistics
    print("\nSummary:")
    print("-" * 75)
    print(f"Total domains tested: {total_domains}")
    print(f"Overall average response time: {(total_avg/total_domains):.2f} ms")
    print(f"Fastest domain: {results[0]['domain']} ({results[0]['avg']:.2f} ms)")
    print(f"Slowest domain: {results[-1]['domain']} ({results[-1]['avg']:.2f} ms)")

if __name__ == '__main__':
    main()