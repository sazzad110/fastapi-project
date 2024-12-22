from fastapi import FastAPI, HTTPException

app = FastAPI()

# Fake database
fake_db = []

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI CRUD Example!"}

# 1. Create
@app.post("/todos/")
def create_todo(id: int, title: str, description: str, completed: bool = False):
    # Check if an item with the same ID already exists
    for todo in fake_db:
        if todo["id"] == id:
            raise HTTPException(status_code=400, detail="Todo with this ID already exists")
    new_todo = {"id": id, "title": title, "description": description, "completed": completed}
    fake_db.append(new_todo)
    return new_todo

# 2. Read all
@app.get("/todos/")
def get_todos():
    return fake_db

# 3. Read one
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in fake_db:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# 4. Update
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, title: str = None, description: str = None, completed: bool = None):
    for todo in fake_db:
        if todo["id"] == todo_id:
            if title is not None:
                todo["title"] = title
            if description is not None:
                todo["description"] = description
            if completed is not None:
                todo["completed"] = completed
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# 5. Delete
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(fake_db):
        if todo["id"] == todo_id:
            fake_db.pop(index)
            return {"message": f"Todo with ID {todo_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")
