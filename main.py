from flask import Flask
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route("/")
def index():
    return "HELLO NGINX"


if __name__ == "__main__":
    http_server = WSGIServer(("127.0.0.1", 8888), app)
    http_server.serve_forever()
