import os
import subprocess
import webbrowser
import signal
import time

def enable_ssh():
    try:
        # Check if SSH is active
        print("Checking SSH service...")
        result = subprocess.run(["sudo", "systemctl", "is-active", "--quiet", "ssh"], check=False)
        
        if result.returncode != 0:
            print("SSH is not active. Enabling SSH...")
            subprocess.run(["sudo", "systemctl", "enable", "--now", "ssh"], check=True)
            print("SSH enabled and started.")
        else:
            print("SSH is already active.")
    except Exception as e:
        print(f"Failed to enable SSH: {e}")

def open_website_forever(url):
    try:
        while True:
            # Open the website
            webbrowser.open(url, new=0)
            print(f"Opened {url}")
            # Wait for a period before reopening (to avoid spamming)
            time.sleep(15)
    except KeyboardInterrupt:
        print("Program interrupted. Exiting...")
        exit(0)

if __name__ == "__main__":
    try:
        # Enable SSH
        enable_ssh()

        # Open website
        website_url = "https://www.microsoft.com/cs-cz/windows/get-windows-11"
        print(f"Opening website: {website_url}")
        open_website_forever(website_url)
    except KeyboardInterrupt:
        print("\nExiting program...")
