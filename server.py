#!/usr/bin/env python3
"""Jednoduchý HTTP server pre statické súbory."""
import http.server
import os

PORT = int(os.environ.get("PORT", 8000))

handler = http.server.SimpleHTTPRequestHandler
handler.extensions_map.update({".js": "application/javascript"})

with http.server.HTTPServer(("0.0.0.0", PORT), handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
