import socket
from concurrent.futures import ThreadPoolExecutor

open_ports = []

COMMON_PORTS = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alt"
}


def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            service = COMMON_PORTS.get(port, "Unknown")
            open_ports.append((port, service))

        sock.close()

    except:
        pass


def run_port_scan(target, start_port=1, end_port=1024):

    global open_ports
    open_ports = []

    with ThreadPoolExecutor(max_workers=100) as executor:

        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, target, port)

    return sorted(open_ports)