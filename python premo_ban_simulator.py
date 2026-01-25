import time
import random
import os
import sys
import webbrowser
from colorama import Fore, Style, init

init(autoreset=True)

CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RED = Fore.RED
GREEN = Fore.GREEN
RESET = Style.RESET_ALL

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def ascii_face():
    art = r"""
        . . . . . . . . . .
      .                     .
    .    ●             ●     .
   .                         .
   .           ▄▄▄           .
   .         ▄█████▄         .
   .        █████████        .
    .        ███████        .
      .        ███        .
        .               .
          . . . . . . .
    """
    print(CYAN + art + RESET)

def header():
    title = "PREMO BAN SIMULATOR"
    print(CYAN + Style.BRIGHT + f"{title:^60}" + RESET)
    print(CYAN + "-" * 60 + RESET)

def stats_block(accounts, proxies, targets):
    print()
    print(YELLOW + f"  Accounts Loaded : {accounts}" + RESET)
    print(YELLOW + f"  Proxies Loaded  : {proxies}" + RESET)
    print(YELLOW + f"  Target Emails   : {targets}" + RESET)
    print(CYAN + "-" * 60 + RESET)

def typing(text, delay=0.03, color=CYAN):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def progress_bar(label="Processing", delay=0.02):
    sys.stdout.write(CYAN + f"{label}: " + RESET)
    sys.stdout.flush()
    for i in range(1, 101):
        bar = f"{i}%"
        sys.stdout.write(CYAN + "\r" + f"{label}: {bar:<4}" + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def generate_complaint_message(number, complaint_type):
    templates = {
        1: "I would like to report this number for scam and fraudulent activities.",
        2: "I would like to report this number for harassment and abusive behavior.",
        3: "I would like to report this number for impersonation and pretending to be someone else.",
        4: "I would like to report this number for sending threats.",
        5: "I would like to report this number for spam and unwanted messages.",
        6: "I would like to report this number for hate speech and offensive content."
    }

    message = f"""
Hello WhatsApp Support,
{templates[complaint_type]}
Phone Number: +{number}
Please review this account.
Thank you.
"""
    return message.strip()

def open_whatsapp_support(number, message):
    encoded_message = message.replace(" ", "%20").replace("\n", "%0A")
    url = f"https://wa.me/{number}?text={encoded_message}"
    webbrowser.open(url)

def main():
    clear()
    ascii_face()
    header()

    accounts_loaded = random.randint(5, 50)
    proxies_loaded = random.randint(1000, 10000)
    targets_loaded = random.randint(5, 25)

    stats_block(accounts_loaded, proxies_loaded, targets_loaded)

    print()
    sys.stdout.write(CYAN + "Enter WhatsApp Number (no + sign): " + RESET)
    number = input().strip()

    if not number.isdigit():
        print(RED + "\nInvalid number format. Exiting..." + RESET)
        return

    print()
    print(YELLOW + "Choose complaint type:" + RESET)
    print(CYAN + """
    1. Scam / Fraud
    2. Harassment / Abuse
    3. Impersonation (Fake Account)
    4. Threats
    5. Spam
    6. Hate / Offensive Content
    """ + RESET)

    sys.stdout.write(CYAN + "Enter choice (1-6): " + RESET)
    choice = input().strip()

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print(RED + "\nInvalid choice. Exiting..." + RESET)
        return

    choice = int(choice)

    clear()
    ascii_face()
    header()
    stats_block(accounts_loaded, proxies_loaded, targets_loaded)

    typing("Generating complaint message...", 0.03)
    progress_bar("Preparing", 0.02)

    message = generate_complaint_message(number, choice)

    print()
    typing("Opening WhatsApp Support...", 0.03, GREEN)
    time.sleep(1)

    open_whatsapp_support(number, message)

    print()
    typing("Done. WhatsApp Support opened successfully.", 0.03, CYAN)

if __name__ == "__main__":
    main()
