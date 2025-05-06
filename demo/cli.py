"""Command-line interface for the demo application."""

import argparse
import sys

from demo.flower import print_flower
from demo.web import run_server

def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(description="Stacklok Demo Python Application")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Server command
    server_parser = subparsers.add_parser("server", help="Run the web server")
    server_parser.add_argument("--host", default="0.0.0.0", help="Host to bind to")
    server_parser.add_argument("--port", type=int, default=5000, help="Port to bind to")
    server_parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    
    # Flower command
    flower_parser = subparsers.add_parser("flower", help="Display ASCII art flowers")
    flower_parser.add_argument("name", nargs="?", help="Name of the flower to display (optional)")
    
    args = parser.parse_args()
    
    if args.command == "server":
        run_server(host=args.host, port=args.port, debug=args.debug)
    elif args.command == "flower":
        print(print_flower(args.name))
    else:
        parser.print_help()
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())