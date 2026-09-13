"""
Nautilus Logistics AI - Robust Local Development HTTP Server (Python)
Features:
- Automatic directory resolution (works from any working directory)
- Explicit MIME type mapping (prevents Firefox & Chrome from blocking ES module .js files)
- Automatic port conflict resolution (tries 8000 -> 8080 -> 5000 -> 3000 -> free port)
- Single Page Application (SPA) routing (serves index.html fallback for client routes)
- Automatic browser launch
"""
import http.server
import socketserver
import os
import sys
import webbrowser

# Explicit MIME type map for standard compliance across Firefox, Chrome, Edge & Safari
MIME_MAP = {
    ".js": "application/javascript; charset=utf-8",
    ".mjs": "application/javascript; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".geojson": "application/json; charset=utf-8",
    ".svg": "image/svg+xml",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".webp": "image/webp",
    ".ico": "image/x-icon",
    ".woff": "font/woff",
    ".woff2": "font/woff2",
    ".ttf": "font/ttf",
    ".html": "text/html; charset=utf-8",
    ".txt": "text/plain; charset=utf-8",
}

# Resolve absolute path to Netlify distributable version directory
CURRENT_FILE_DIR = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR_NAME = "Netlify distributable version"

if os.path.basename(CURRENT_FILE_DIR) == "python_engine":
    DIST_DIR = os.path.abspath(os.path.join(CURRENT_FILE_DIR, "..", TARGET_DIR_NAME))
else:
    DIST_DIR = os.path.abspath(os.path.join(CURRENT_FILE_DIR, TARGET_DIR_NAME))

# Fallback checks
if not os.path.exists(DIST_DIR):
    alt_dir = os.path.join(os.getcwd(), TARGET_DIR_NAME)
    if os.path.exists(alt_dir):
        DIST_DIR = alt_dir
    else:
        # Fallback to dist if present
        fallback_dist = os.path.abspath(os.path.join(CURRENT_FILE_DIR, "dist"))
        if os.path.exists(fallback_dist):
            DIST_DIR = fallback_dist
        else:
            print(f"[Error] '{TARGET_DIR_NAME}' folder not found at: {DIST_DIR}")
            print("Please build the app before running the server.")
            sys.exit(1)

class SPARequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIST_DIR, **kwargs)

    def guess_type(self, path):
        # Prevent Windows Registry from polluting JS/CSS MIME types
        base, ext = os.path.splitext(path.lower())
        if ext in MIME_MAP:
            return MIME_MAP[ext]
        return super().guess_type(path)

    def do_GET(self):
        # Normalize requested path
        clean_path = self.path.split("?")[0].split("#")[0].lstrip("/")
        file_path = os.path.join(DIST_DIR, clean_path)

        # If file doesn't exist and not an explicit asset request, fallback to index.html (SPA routing)
        if not os.path.exists(file_path) and not clean_path.startswith("assets/"):
            self.path = "/index.html"

        return super().do_GET()

    def end_headers(self):
        # Enable CORS and disable aggressive caching during local development
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache, must-revalidate")
        super().end_headers()

    def log_message(self, format, *args):
        # Clean terminal logging
        sys.stdout.write(f"[{self.log_date_time_string()}] {args[0]} -> {args[1]}\n")

def find_available_port(preferred_ports=[8000, 8080, 5173, 5000, 3000]):
    import socket
    for port in preferred_ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("127.0.0.1", port)) != 0:
                return port
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]

def get_local_ip():
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def run_server():
    socketserver.TCPServer.allow_reuse_address = True
    port = find_available_port()
    server_address = ("0.0.0.0", port)
    
    try:
        httpd = socketserver.TCPServer(server_address, SPARequestHandler)
    except OSError:
        port = find_available_port([8081, 8082, 8083, 0])
        server_address = ("0.0.0.0", port)
        httpd = socketserver.TCPServer(server_address, SPARequestHandler)

    local_url = f"http://localhost:{port}"
    lan_ip = get_local_ip()
    network_url = f"http://{lan_ip}:{port}"

    print("=" * 68)
    print("  [NAUTILUS] Logistics AI - Universal Local & Network Server")
    print(f"  [PATH] Serving Directory: {DIST_DIR}")
    print(f"  [PC]   Local Browser:     {local_url}")
    print(f"  [LAN]  Mobile / Wi-Fi:    {network_url}")
    print("=" * 68)
    print("  -> Open the Mobile / Wi-Fi URL on any phone on the same network!")
    print("  -> Press Ctrl+C to stop the server.")
    print("=" * 68)

    try:
        webbrowser.open(local_url)
    except Exception:
        pass

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[INFO] Server stopped gracefully.")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
