from fastapi import FastAPI
from stem.control import Controller
from uvicorn import run

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

def create_hidden_service(controller, port):
    response = controller.create_ephemeral_hidden_service({80: port}, await_publication=True)
    print(f"Created host: {response.service_id}.onion")

if __name__ == "__main__":
    local_port = 5000
    tor_control_port = 9051

    # Start the FastAPI app
    run(app, host="127.0.0.1", port=local_port)

    # Connect to the Tor control port and authenticate
    with Controller.from_port(port=tor_control_port) as controller:
        controller.authenticate()

        # Create the hidden service and print the onion address
        create_hidden_service(controller, local_port)
