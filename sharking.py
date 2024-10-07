from scapy.all import rdpcap, DNSQR, DNSRR, IP, TCP

# Load the PCAP file
packets = rdpcap('TracingTheTrail.pcap')

# Initialize dictionaries to store DNS queries and HTTP requests
dns_queries = {}
http_requests = []

# Process packets to extract DNS queries, DNS responses, and HTTP requests
for packet in packets:
    if packet.haslayer(DNSQR):  # DNS Question Record
        dns_query = packet[DNSQR].qname.decode()
        dns_queries[dns_query] = None  # Initialize with None

    if packet.haslayer(DNSRR):  # DNS Resource Record (Response)
        dns_response = packet[DNSRR].rrname.decode()
        if dns_response in dns_queries:
            dns_queries[dns_response] = packet[DNSRR].rdata.decode()  # Store the resolved IP

    if packet.haslayer(TCP) and packet.haslayer(IP):  # Look for HTTP requests
        if packet[TCP].dport == 80:  # Port 80 is typically used for HTTP
            ip_dst = packet[IP].dst
            http_requests.append(ip_dst)

# Extract only the non-empty DNS queries (those with responses)
resolved_dns = {k: v for k, v in dns_queries.items() if v}

print("Resolved DNS Queries:")
print(resolved_dns)

print("\nHTTP Requests:")
print(http_requests)
