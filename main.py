from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"id": item_id, "name": f"Item {item_id}"

