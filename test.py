from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, needy: str , item_o_id:int=10 , item_date:str | None=None):      # hit api :http://127.0.0.1:8000/items/item-foo/?needy=somethingneedy&item_o_id=20
    items = {'item_id':item_id}
    return items
