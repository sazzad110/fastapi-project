from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None=None
    price: float
    tax: float | None=None

app = FastAPI()

@app.get("/items/")
async def get_item():
    return {'test':'okay'}

@app.post("/items/")
async def create_item(item: Item):
    return item

