from fastapi import FastAPI 
from fastapi.params import Body

app=FastAPI()

@app.get('/') 
async def home(): 
    return {'hellow' : "Deepraj"}

app.post('/createPost')
def create_post(payload: dict=Body(...)) : 
    param= payload   
    return {"meassage" : "hellow my name is deepraj" }