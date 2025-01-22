# Network Scanner

## Description
The Network Scanner is a Python-based command-line tool designed for network administrators and cybersecurity professionals to efficiently scan local networks and retrieve information about active devices. It utilizes the Scapy library to perform ARP requests, allowing it to detect connected devices by their IP and MAC addresses. Lightweight, flexible, and easy to use, this tool is ideal for quick network audits or security assessments.

---

## Key Features
1. **Custom IP Range Scanning**:
   - Accepts user-specified IP ranges through command-line arguments, enabling targeted scans (e.g., `192.168.1.0/24` or `10.0.0.0/24`).
   
2. **Efficient Device Detection**:
   - Combines ARP requests with Ethernet broadcast frames to identify active devices in the network.

3. **Clear and Organized Output**:
   - Displays a tabular list of detected devices, including their IP addresses and corresponding MAC addresses.

4. **Command-Line Argument Parsing**:
   - Utilizes the `argparse` module for user-friendly input prompts and error handling, ensuring a seamless user experience.

---

## How It Works
1. The user specifies the target IP range via the `-t` or `--target` argument.
2. The tool constructs ARP requests and broadcasts them over the network.
3. Responses from active devices are collected, processed, and formatted into a list of dictionaries containing IP and MAC addresses.
4. Results are displayed in a clean, tabular format for easy interpretation.

---

## Technologies Used
- **Python**: Core language for scripting and logic implementation.
- **Scapy Library**: For ARP request generation, Ethernet broadcasting, and network communication.
- **Argparse Module**: To parse and validate user inputs from the command line.

---

## Usage Example
Run the script from the command line using the following syntax:
```bash
python Network_Scanner.py -t 192.168.1.0/24
