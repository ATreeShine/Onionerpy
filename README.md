# Tor Hidden Service with FastAPI

This Python script uses FastAPI and Stem to create a Tor hidden service. The service runs a simple web server that responds with "Hello, World" to HTTP GET requests at the root ("/").

## Prerequisites

To run this script, you need:

- Python 3.6 or later
- FastAPI
- Uvicorn
- Stem

You also need to have Tor installed and running on your machine.

## Installation

First, install the required Python libraries with pip:

```bash
pip install fastapi uvicorn stem
```
Then, clone this repository or download the script to your local machine.
## Usage
To start the service, run the script with Python:
bash
python script_name.py

Replace script_name.py with the name of the script file.
The script will start a FastAPI application on localhost, port 5000, and create a Tor hidden service that forwards requests to this server. The onion address of the service will be printed to the console.
You can access the service by navigating to this address in the Tor Browser.
## License
This project is licensed under the MIT License. See the LICENSE file for details.

Please replace "script_name.py" with the actual name of your script file. Also, note that this README assumes that the user has Python and Tor installed and knows how to use them. If this is not the case, you may want to add more detailed instructions or links to relevant resources[1][2][3][4]
Please replace "main.py" with the actual name of your script file. Also, note that this README assumes that the user has Python and Tor installed and knows how to use them. If this is not the case, you may want to add more detailed instructions or links to relevant resources
