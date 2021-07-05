import requests
import time
waterLevelUpper = 10
while True:
    response = requests.get(
        "http://0.0.0.0:8000/upperStats/"+str(waterLevelUpper))
    print(response.text)
    time.sleep(5)
