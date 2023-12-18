import os
import subprocess
import time

# Install dependencies
subprocess.run(["apt", "install", "figlet", "-y"])
subprocess.run(["apt", "install", "tor", "-y"])
subprocess.run(["apt", "install", "wget", "-y"])
subprocess.run(["apt", "install", "php", "-y"])
subprocess.run(["apt", "install", "nano", "-y"])

# Clear the screen
subprocess.run(["clear"])

# Display the banner
subprocess.run(["figlet", "-f", "slant", "HostOnion"])
time.sleep(1)

# Author information
print("\033[1;91m  Author   \033[1;90m: \033[1;95mAllowedical\n")

# Start PHP server
php_process = subprocess.Popen(["php", "-S", "127.0.0.1:8080"])
print("\033[1;95mPhp server is up")
print("\033[1;96mYou can check your server by accessing localhost:8080")

# Configure Tor hidden service
hidden_service_dir = "/data/data/com.termux/files/usr/var/lib/tor/hidden_service"
torrc_path = "/data/data/com.termux/files/usr/etc/tor/torrc"

# Create hidden_service directory if it doesn't exist
os.makedirs(hidden_service_dir, exist_ok=True)

# Remove existing hostname and torrc files if they exist
if os.path.exists(os.path.join(hidden_service_dir, "hostname")):
    os.remove(os.path.join(hidden_service_dir, "hostname"))

if os.path.exists(torrc_path):
    os.remove(torrc_path)

# Download the torrc configuration file
subprocess.run(["wget", "https://raw.githubusercontent.com/Deauthxploit/Nothing_much/main/torrc", "-O", torrc_path])

# Start Tor
tor_process = subprocess.Popen(["tor"])
time.sleep(60)

# Display the .onion hostname
with open(os.path.join(hidden_service_dir, "hostname"), "r") as hostname_file:
    hostname = hostname_file.read().strip()
    print(f"\033[1;32mYour Onion Site is Ready !!\n\033[91m{hostname}\033[39m")

# Keep the script running until interrupted
try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    # Terminate the PHP and Tor processes
    php_process.terminate()
    tor_process.terminate()
    print("\nExiting HostOnion")
