from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, needy: str):      # hit api : http://127.0.0.1:8000/items/item-foo/?needy=somethingneedy
    items = {'item_id':item_id}
    return items
