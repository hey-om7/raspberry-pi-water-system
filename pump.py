import requests
import time
waterAvailable = True
while True:
    response = requests.get(
        "http://0.0.0.0:8000/waterAvailable/"+str(waterAvailable))
    print(response.text)
    # i = i+1
    time.sleep(5)
