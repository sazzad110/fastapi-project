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

@app.put("/items/{item_id}")
async def update_item(item_id: int , item: Item, temp: str):
    result = {"item_id":item_id , **item.dict()}
    if temp:
        result.update({"temporary key":temp})
    return result

