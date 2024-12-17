import requests
import time

def ping_site(url, interval):
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{time.ctime()} - Site is up")
        else:
            print(f"{time.ctime()} - Site is down (Status Code: {response.status_code})")
        time.sleep(interval)

if __name__ == "__main__":
    url = "http://example.com"
    interval = 10  # Interval in seconds
    ping_site(url, interval)
