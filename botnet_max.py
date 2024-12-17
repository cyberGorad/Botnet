import requests
import time

def flood_site(url, interval):
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"{time.ctime()} - Site is up")
            else:
                print(f"{time.ctime()} - Site is down (Status Code: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"{time.ctime()} - Error: {e}")
        time.sleep(interval)

if __name__ == "__main__":
    url = "http://example.com"
    interval = 0.01  # Interval in seconds
    flood_site(url, interval)
