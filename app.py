from flask import Flask, request
import socket
import os

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    return f"""
    <h1>🚀 Kubernetes DevOps App</h1>
    <p><b>Hostname:</b> {hostname}</p>
    <p><b>Pod IP:</b> {ip}</p>
    <p><b>Client IP:</b> {request.remote_addr}</p>
    <p><b>Environment:</b> {os.getenv('ENV', 'Not Set')}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
