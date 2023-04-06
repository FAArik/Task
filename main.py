from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from extract import *
import os


SECRET = os.getenv("SECRET")

#
app = FastAPI()

class Msg(BaseModel):
    msg: str
    secret: str

@app.get("/")
async def root():   
    return {"message": "Hello World. Welcome to FastAPI!"}


@app.get("/javascript")
async def javascript(url:str):
    driver=createDriver()
    homepage = javascr(driver,url)

    driver.close()
    return homepage

@app.get("/image")
async def image(url:str):
    driver=createDriver()
    homepage = imageres(driver,url)
    driver.close()
    return homepage

@app.get("/translate")
async def translate(url:str):
    driver=createDriver()
    homepage = language(driver,url)
    driver.close()
    return homepage

@app.get("/wrongsite")
async def wrongsite(url:str):
    driver=createDriver()
    homepage= wrong(driver,url)
    driver.close()
    return homepage


    


