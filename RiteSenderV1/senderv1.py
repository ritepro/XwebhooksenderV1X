import requests
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def send_webhook(webhook_url, message, times):
    for _ in range(times):
        payload = {
            "content": message,
            "embeds": [
                {
                    "title": f"{Fore.MAGENTA}Made By Rite{Style.RESET_ALL}",
                    "description": f"{Fore.MAGENTA}OPEN SOURSE SENDER V1{Style.RESET_ALL}"
                }
            ]
        }

        headers = {"Content-Type": "application/json"}

        response = requests.post(webhook_url, json=payload, headers=headers)

        if response.status_code == 204:
            print(f"{Fore.GREEN}Message sent successfully ({_ + 1}/{times}){Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Failed to send message ({_ + 1}/{times}){Style.RESET_ALL}")

def main():
    webhook_url = input("Input Discord webhook URL: ")
    message = input("Input message to send on webhook: ")
    times = int(input("Amount of times to send: "))

    send_webhook(webhook_url, message, times)

    print("Script execution completed.")
    input("Press Enter to close the console window...")

if __name__ == "__main__":
    while True:
        main()
