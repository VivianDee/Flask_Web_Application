#!/usr/bin/python3
from website import create_app

"""
    Run my Flask applicaton and set up a webserver
    entry point for my app
"""

app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
