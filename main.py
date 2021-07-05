from fastapi import FastAPI

from pydantic import BaseModel
from typing import Optional

from pydantic.tools import T
import time


app = FastAPI()


@app.get("/")
def read_route():
    return {"greetings": "Welcome and success"}


@app.get("/upperTankLevel/{text}")
def upperTankLevel(text: int):
    if(text < 100):
        val = False
    else:
        val = True
    settingUpperTankFull(val)
    return "Got UpperTankVal"


def settingUpperTankFull(val: bool):
    global lowerTankTime
    print("-->"+str(lowerTankTime))
    global upperTankFull
    upperTankFull = val


@app.get("/lowerTankLevel/{val}")
def lowerTankLevel(val: bool):
    settingLowerTankFull(val)
    if(upperTankFull):
        if(lowerTankFull):
            return "Both Tanks Filled"
        else:
            return "FillLowerTank"
    else:
        return "UpperTankFill"


# lowerTankTime = time.time()
# global lowerTankTime


def settingLowerTankFull(val: bool):
    global lowerTankFull
    global lowerTankTime
    lowerTankTime = time.time()
    lowerTankFull = val


lowerTankFull = True
upperTankFull = True


@app.get("/waterAvailable/{waterAvailable}")
def waterAvailable(waterAvailable: bool):
    global lowerTankTime
    print("allalalal", lowerTankTime)
    if(time.time()-lowerTankTime < 10):
        if(waterAvailable and ((not upperTankFull) or (not lowerTankFull))):
            return "TurnPumpOn"
        else:
            return "TurnPumpOff"
    else:
        return "NoConnectionTurnPumpOff"


# waterAvailable=true/false
# lowertankFull=true/false
# upperTankFull
