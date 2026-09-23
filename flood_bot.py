#Cookie

import urllib.request
import threading

url = "http://localhost:8080"

def launch_requests():
    print("Bot thread started...")
    while True:
        try:
            urllib.request.urlopen(url)
        except Exception as e:
            print(f"Server overloaded, unresponsive: {e}")

