from fastapi import FastAPI
from stem.control import Controller

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    from uvicorn import run
    run(app, host="127.0.0.1", port=5000)

    controller = Controller.from_port(port=9051)
    controller.authenticate()

    response = controller.create_ephemeral_hidden_service({80: 5000}, await_publication=True)
    print("Created host: {}.onion".format(response.service_id))
