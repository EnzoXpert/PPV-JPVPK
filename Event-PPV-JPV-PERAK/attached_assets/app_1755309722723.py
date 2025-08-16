from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='.', static_url_path='')

# Serve the main page
@app.route('/')
def index():
    return send_from_directory('.', 'lucky-draw.html')

# Serve any other static file in the project folder (css, js, images if present)
@app.route('/<path:path>')
def static_proxy(path):
    # Prevent directory traversal
    safe_path = os.path.normpath(path)
    return send_from_directory('.', safe_path)

if __name__ == '__main__':
    # Bind to all interfaces so other devices on the network can access (useful for testing on mobile)
    app.run(host='0.0.0.0', port=8000, debug=True)
