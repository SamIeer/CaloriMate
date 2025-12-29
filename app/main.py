from fastapi import FastAPI

app = FastAPI()   # initialise a fastapi app 

@app.get("/")     # creating a path operations (GET, POST)
async def root(): # A async functions defines the path operation
    return {"message": "Hello World!"} # returning the content

WOrking should be done 