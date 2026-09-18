from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime

def analyze(pkt):
    if IP in pkt:
        proto = "TCP" if TCP in pkt else "UDP" if UDP in pkt else "Other"
        line = f"[{datetime.now().strftime('%H:%M:%S')}] {pkt[IP].src} -> {pkt[IP].dst} | {proto} | {len(pkt)} bytes"
        print(line)
        with open("packets.txt", "a") as f:
            f.write(line + "\n")

print("=== Packet Analyzer Started (Educational) ===")
open("packets.txt", "w").write("Packet Capture Log\n")
sniff(filter="ip", prn=analyze, count=20, store=0)
print("\nDone! Task Completed - saved to packets.txt")