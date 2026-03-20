#!/usr/bin/env python
"""Start the Django Triage Manager GUI with custom configuration."""

import os
import socket
import threading
import time
import webbrowser
import argparse
from django.core.management import execute_from_command_line


def run_django(host, port, settings_module):
    """
    Run the Django development server.
    
    Args:
        host: Host address to bind to
        port: Port number to listen on
        settings_module: Django settings module path
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
    
    execute_from_command_line([
        "manage.py", 
        "runserver", 
        f"{host}:{port}", 
        "--noreload", 
        "--insecure"
    ])


def wait_for_server_and_open_browser(host, port):
    """Wait for the server to be ready and then open the browser."""
    url = f"http://{host}:{port}"
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            result = sock.connect_ex((host, int(port)))
            if result == 0:
                webbrowser.open(url)
                break
        time.sleep(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start the Django Triage Manager GUI.")
    
    parser.add_argument(
        "--port", 
        type=int, 
        default=8003, 
        help="Port to run the server on (default: 8003)"
    )
    parser.add_argument(
        "--config-file", 
        type=str, 
        default="", 
        help="Config YAML file path"
    )
    
    args = parser.parse_args()
    host = "127.0.0.1"
    
    # Store config file path in environment variable for settings.py to use
    if args.config_file:
        os.environ["EUD_CONFIG_FILE"] = args.config_file

    # Kick off the browser thread with the dynamic port
    threading.Thread(
        target=wait_for_server_and_open_browser, 
        args=(host, args.port), 
        daemon=True
    ).start()

    # Run the server with the dynamic port
    run_django(host, args.port, "eud_gui.settings")
