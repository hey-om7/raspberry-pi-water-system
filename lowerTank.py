import requests
import time
fullStatus = True
while True:
    response = requests.get(
        "http://0.0.0.0:8000/lowerTankLevel/"+str(fullStatus))
    print(response.text)
    time.sleep(5)
