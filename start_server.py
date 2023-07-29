# start_server.py
import yaml
import http.server
import socketserver

def start_local_server():
    # Read the configuration from the YAML file
    with open("config.yml", "r") as config_file:
        config = yaml.safe_load(config_file)

    # Get the port and directory from the configuration
    port = config.get("port", 8000)
    directory = config.get("directory", ".")

    # Start the local web server
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Local server started on port {port}. Serving from directory: {directory}")
        httpd.serve_forever()

if __name__ == "__main__":
    start_local_server()
