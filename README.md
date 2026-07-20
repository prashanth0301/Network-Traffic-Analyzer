# Network Traffic Analyzer

A professional Python-based **Network Traffic Analyzer** built using **Scapy**. The tool captures live network packets, analyzes traffic in real time, displays protocol statistics, and generates detailed reports in both CSV and text formats.

---

## Features

* Capture live network traffic
* Automatic network interface selection
* Protocol filtering

  * All Packets
  * TCP
  * UDP
  * ICMP
  * ARP
* Real-time packet monitoring
* Protocol detection
* Source and Destination IP analysis
* Live traffic statistics
* Packet size analysis
* Automatic CSV report generation
* Automatic traffic summary report generation
* Easy-to-read console output

---

## Technologies Used

* Python 3
* Scapy
* Colorama
* Socket
* Collections
* CSV
* Time

---

## Project Structure

```
Network Traffic Analyzer/
│
├── network_traffic_analyzer.py
├── interface_selection.py
├── packet_capture.py
├── packet_analysis.py
├── packet_utils.py
├── statistics.py
├── report_generator.py
├── requirements.txt
├── README.md
├── notes.md
├── architecture.txt
├── .gitignore
│
├── reports/
│   ├── captured_packets.csv
│   └── traffic_summary.txt
│
└── assets/
    ├── banner.png
    ├── architecture.png
    ├── interface_selection.png
    ├── packet_capture.png
    ├── live_statistics.png
    └── summary.png
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/network-traffic-analyzer.git
```

Move into the project folder

```bash
cd network-traffic-analyzer
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
py network_traffic_analyzer.py
```

---

## How It Works

1. Display available network interfaces.
2. Select the interface to monitor.
3. Choose a capture filter.
4. Enter the number of packets to capture.
5. Capture and analyze live packets.
6. Display live statistics.
7. Generate CSV and summary reports.

---

## Sample Output

* Live packet capture
* Protocol detection
* Source and destination IP addresses
* Port information
* Packet sizes
* Live statistics
* Traffic summary
* CSV report generation

---

## Future Enhancements

* DNS packet analysis
* HTTP packet parsing
* Geo-IP lookup
* MAC vendor identification
* PCAP file export
* Graphical dashboard
* Bandwidth monitoring
* Real-time packet visualization

---

## Learning Outcomes

This project demonstrates practical knowledge of:

* Network packet capture
* Packet analysis
* Network protocols
* Scapy
* Python networking
* Traffic monitoring
* File handling
* Report generation
* Real-time statistics

---

## Author

**Prashanth Reddy Y**

Cybersecurity & Networking Enthusiast
