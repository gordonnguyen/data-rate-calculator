import sys
import pyshark

def calculate_data_rate(pcap_file):
  """
  Calculates and prints download data rate from a pcap file.
  """
  capture = pyshark.FileCapture(pcap_file, display_filter='ip.src==104.198.203.13 && tcp.port==443')
  # Filter packets to only 104.198.203.13

  total_length = 0
  start_time = capture[0].sniff_timestamp

  counter = 0
  for packet in capture:
    total_length += int(packet.length)
    counter += 1    # Counter for last package ID

  end_time = capture[counter-1].sniff_timestamp

  time_interval = float(end_time) - float(start_time)
  data_rate = (total_length / time_interval) / (10**6)  # Convert to Mbps
  print(f"Download Data Rate: {data_rate:.2f} Mbps")

if __name__ == "__main__":    
    if len(sys.argv) != 2:
        print("Usage: python3 Har_Nguyen_UID.py <har_file>")
    else:
        calculate_data_rate(sys.argv[1])