from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.books.routes import book_router
from src.db.main import init_db

@asynccontextmanager
async def life_span(app:FastAPI):
    print(f"Server is starting...")
    await init_db()
    yield
    print(f"Server is stoping...")

version = "v1"

app = FastAPI(
    title= "Book APi",
    description="A rest api for book preview web service",
    version=version,
    lifespan=life_span,
)

app.include_router(book_router,prefix=f"/api/{version}/books",tags=["books"])