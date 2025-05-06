"""Web server functionality for the demo application."""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

def run_server(host='0.0.0.0', port=5000, debug=False):
    """Run the Flask web server."""
    app.run(host=host, port=port, debug=debug)