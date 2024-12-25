from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None , short: bool = False):
    items = {'item_id':item_id}
    if q:
        items.update({'q':q})
    if not short:
        items.update({'description':'This is an amzing des with logn'})
    return items