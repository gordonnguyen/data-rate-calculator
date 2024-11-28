import json
import sys

def calculate_data_rate(har_file):
    with open(har_file, 'r') as file:
        har_data = json.load(file)

    total_size = sum(entry['response']['content']['size'] for entry in har_data['log']['entries'])
    onload_time = har_data['log']['pages'][0]['pageTimings']['onLoad']

    data_rate_mbps = (total_size / onload_time) * 1000 / 10**6
    print(f"Download Data Rate: {data_rate_mbps:.2f} Mbps")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 Har_Nguyen_UID.py <har_file>")
    else:
        calculate_data_rate(sys.argv[1])