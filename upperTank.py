import requests
import time
level = 100
while True:
    response = requests.get(
        "http://0.0.0.0:8000/upperTankLevel/"+str(level))
    print(response.text)
    time.sleep(5)
