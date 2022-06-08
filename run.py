import os
from app.app import create_app
from app.config import Config
from gevent.pywsgi import WSGIServer

app = create_app(Config)

# Define host and port for the app
# Tell the app how and where to run
if __name__ == "__main__":
    app.debug = True

    # Create WSGI server with params for Repl.it (IP 0.0.0.0, port 8080)
    # for our Flask app
    http_server = WSGIServer(('0.0.0.0', 8080), app)

    # Start WSGI server
    http_server.serve_forever()
