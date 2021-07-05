import requests
import time
available = 0  # 0 for no 1 for yes
while True:
    response = requests.get(
        "http://0.0.0.0:8000/waterAvailable/"+str(available))
    print(response.text)
    time.sleep(5)
