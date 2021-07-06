from fastapi import FastAPI

from pydantic import BaseModel
from typing import Optional

from pydantic.tools import T
import time

from datetime import datetime
import os

app = FastAPI()


def saveText(valueRec: str, fileName: str):
    current_time = str(time.time())
    _tempDir = os.path.realpath(__file__)
    _tempLength = _tempDir.split("/")[-1]
    dir = _tempDir[0: len(_tempDir)-len(_tempLength)] + \
        fileName+".txt"
    file_object = open(dir, 'w')
    file_object.write(valueRec+"--"+current_time)
    file_object.close()


def getSavedText(fileName: str):
    file1 = open(fileName+".txt", "r")
    list1 = file1.readlines()
    list2 = list1[0].split("--")
    file1.close()
    return list2


@app.get("/")
def read_route():
    return {"greetings": "Welcome and success"}


@app.get("/upperTankLevel/{value}")
def upperTankLevel(value: str):
    saveText(value, "upperTankVal")
    return "Got UpperTankValue", value


@app.get("/lowerTankLevel/{value}")
def lowerTankLevel(value: str):
    if(int(getSavedText('upperTankVal')[0]) < 100):
        saveText(value, "lowerTankVal")
        return "Filling Upper Mode Pulley"
    else:
        saveText(value, "lowerTankVal")
        return "Filling Lower Mode Pulley"


@app.get("/pump/{value}")
def waterAvail(value: str):
    saveText(value, 'pump')
    upper = True
    lower = True

    if((int(getSavedText('upperTankVal')[0]) < 100) or (int(getSavedText('lowerTankVal')[0]) < 100)) and int(getSavedText('pump')[0]) == 1:
        print('here1')
        if (time.time()-(float(getSavedText('upperTankVal')[1])) > 10.0):
            # print(time.time()-(float(getSavedText('upperTankVal')[1])))
            upper = False
        if (time.time()-(float(getSavedText('lowerTankVal')[1])) > 10.0):
            # print('here4')
            lower = False
        if(not upper) and (not lower):
            return "Turning Motor Off"
        else:
            # print('here2')
            return "Turning Motor On"
    else:
        return "Turning Motor Off"

# lower,upper,pump


@app.get("/getStats/{text}")
def gettingWaterStatus(text: str):
    if(text == "upper"):
        val = getSavedText('upperTankVal')[0]
    elif(text == "lower"):
        val = getSavedText('lowerTankVal')[0]
    elif(text == "pump"):
        val = getSavedText('pump')[0]

    return val
