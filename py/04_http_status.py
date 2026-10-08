import urllib.request
import time

url = "https://example.com"

try:
    start_time = time.time()

    response = urllib.request.urlopen(url, timeout=10)

    end_time = time.time()

    status_code = response.status
    response_time = end_time - start_time

    print("Website:", url)
    print("Status Code:", status_code)
    print("Response Time:", round(response_time, 3), "seconds")

except Exception as e:
    print("Error:", e)