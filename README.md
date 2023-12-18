# HostOnion - Tor Hidden Service 


HostOnion is a Python script that automates the setup of a Tor hidden service and starts a local PHP server to serve content over the Tor network.

## Requirements

- Python 3.x
- Tor installed on your system
- PHP installed on your system
- `wget` command-line utility
- `nano` text editor (optional for editing configurations)

## Installation

Before running the script, ensure you have the required dependencies installed on your system. You can install them using the following commands:

```bash
sudo apt-get update
sudo apt-get install tor php wget nano -y
```

## How to Run
Clone the repository or download the Python script to your local machine.
Make sure the script has execute permissions:
`
chmod +x hostonion.py
`
Run the script:
`
python3 hostonion.py
`
The script will perform the following actions:
Start a PHP server on localhost at port 8080.
Configure Tor to create a hidden service that forwards traffic to the PHP server.
Display the .onion address for your hidden service.

## How it works
The script automates the process of setting up a Tor hidden service by:
Installing necessary packages like tor, php, and wget.
Starting a PHP server that listens on 127.0.0.1:8080.
Configuring Tor with a new hidden service by downloading a torrc configuration file and placing it in the appropriate directory.
Restarting the Tor service to apply the new configuration.
Displaying the generated .onion address which you can use to access your service via the Tor browser.

### SAMPLE OUTPUT
Php server is up
You can check your server by accessing localhost:8080
Your Onion Site is Ready !!
http://youronionsiteaddress.onion
