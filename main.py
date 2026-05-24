from colorama import Fore, init
from scanner.port_scanner import run_port_scan
from scanner.banner_grabber import grab_banner
from scanner.header_checker import check_headers
from scanner.ssl_checker import check_ssl
from scanner.vulnerability_checker import check_vulnerability
from reports.report_generator import generate_report

init(autoreset=True)


print(Fore.GREEN + """

███████╗███████╗ ██████╗██╗   ██╗██████╗ ███████╗
██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗██╔════╝
███████╗█████╗  ██║     ██║   ██║██████╔╝█████╗
╚════██║██╔══╝  ██║     ██║   ██║██╔══██╗██╔══╝
███████║███████╗╚██████╗╚██████╔╝██║  ██║███████╗
╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝

""")


target = input("Enter Target IP or Domain: ")

print(Fore.CYAN + "\n[+] Scanning Open Ports...")

ports = run_port_scan(target)

print(Fore.GREEN + f"[+] Found {len(ports)} open ports")

banners = {}
vulnerabilities = {}

for port, service in ports:
    banner = grab_banner(target, port)

    banners[port] = banner

    vulnerability = check_vulnerability(banner)

    vulnerabilities[port] = vulnerability

    print(Fore.YELLOW + f"Port {port} ({service})")
    print(Fore.WHITE + f"Banner: {banner}")
    print(Fore.RED + f"Vulnerability: {vulnerability}\n")


url = f"http://{target}"

print(Fore.CYAN + "[+] Checking Security Headers...")

headers = check_headers(url)

for header, status in headers.items():
    print(Fore.WHITE + f"{header}: {status}")


print(Fore.CYAN + "\n[+] Checking SSL Certificate...")

ssl_result = check_ssl(target)

for key, value in ssl_result.items():
    print(Fore.WHITE + f"{key}: {value}")


print(Fore.CYAN + "\n[+] Generating Report...")

report = generate_report(
    target,
    ports,
    banners,
    headers,
    ssl_result,
    vulnerabilities
)

print(Fore.GREEN + f"\n[+] Report Saved: {report}")