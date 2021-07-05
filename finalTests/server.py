from fastapi import FastAPI

from pydantic import BaseModel
from typing import Optional

from pydantic.tools import T
import time


app = FastAPI()


@app.get("/")
def abra():
    return 'Program home page'


@app.get("/waterAvailable/{text}")
def abra1(text: int):
    makingPumpTimeGlobal(time.time())
    return returningFunction()


def makingPumpTimeGlobal(time: int):
    global receivedReqTime
    receivedReqTime = time


def returningFunction():
    if(time.time()-receivedReqTime > 10):
        return 'lost connection turn off'
    else:
        return 'decide from sensors'


@app.get("/upperStats/{text}")
def abra1(text: int):
    makingPumpTimeGlobal(time.time())
    return returningFunction()


def makingPumpTimeGlobal(time: int):
    global receivedReqTime
    receivedReqTime = time
