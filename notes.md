# Network Traffic Analyzer - Project Notes

## Project Overview

The Network Traffic Analyzer is a Python-based application that captures live network traffic using Scapy. It analyzes packets in real time, displays important network information, maintains traffic statistics, and generates reports for later analysis.

---

# Project Workflow

1. Start the application.
2. Display available network interfaces.
3. Select a network interface.
4. Choose a capture filter.
5. Capture live packets.
6. Analyze each packet.
7. Display packet information.
8. Update live statistics.
9. Save packet information to a CSV report.
10. Generate a traffic summary report.

---

# Module Description

## network_traffic_analyzer.py

Main controller of the project.

Responsibilities:

* Displays project banner
* Calls interface selection
* Accepts capture filter
* Starts packet capture
* Coordinates all modules
* Generates reports

---

## interface_selection.py

Responsible for selecting the network interface.

Functions:

* Display all available interfaces
* Show interface IP addresses
* Allow user selection
* Return selected interface

---

## packet_capture.py

Responsible for capturing packets.

Features:

* Starts Scapy packet capture
* Supports protocol filters
* Accepts packet limit
* Processes packets one by one

---

## packet_analysis.py

Analyzes every captured packet.

Extracts:

* Protocol
* Source IP
* Destination IP
* Source Port
* Destination Port
* Packet Size

---

## packet_utils.py

Contains helper functions.

Responsibilities:

* Display packet information
* Format console output
* Improve code reusability

---

## statistics.py

Maintains live traffic statistics.

Tracks:

* Total packets
* Total bytes
* Protocol distribution
* Top source IP addresses
* Top destination IP addresses
* Average packet size
* Capture duration

Displays live statistics after every configured interval.

---

## report_generator.py

Generates project reports.

Creates:

* CSV packet report
* Traffic summary report

Stores reports inside the **reports/** directory.

---

# Reports Generated

## Packet Report

Contains:

* Timestamp
* Protocol
* Source IP
* Destination IP
* Source Port
* Destination Port
* Packet Size

---

## Traffic Summary

Contains:

* Total packets
* Total bytes
* Capture duration
* Average packet size
* Protocol distribution
* Top source IP addresses
* Top destination IP addresses

---

# Libraries Used

* Scapy
* Colorama
* Socket
* Collections
* CSV
* Time

---

# Skills Demonstrated

* Python Programming
* Network Packet Analysis
* Packet Capture
* Protocol Analysis
* Report Generation
* Real-Time Monitoring
* Modular Programming
* File Handling
* Data Analysis

---

# Possible Future Improvements

* DNS packet parsing
* HTTP packet analysis
* HTTPS session tracking
* MAC vendor lookup
* PCAP export
* Geo-IP lookup
* Traffic graphs
* GUI interface
* Bandwidth monitoring
* Intrusion detection

---

# Conclusion

This project demonstrates the implementation of a modular Network Traffic Analyzer capable of capturing, analyzing, and reporting live network traffic. It strengthens practical knowledge of Python networking, packet analysis, and real-time traffic monitoring while following a clean and maintainable project structure.
