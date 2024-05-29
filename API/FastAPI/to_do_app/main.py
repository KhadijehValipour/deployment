from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from typing import List

# FastAPI setup
app = FastAPI()
# Database setup
DATABASE_URL = "todo.db"

def get_db():
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row  # To return rows as dictionaries
    return conn

def initialize_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        time TEXT NOT NULL,
        status BOOLEAN NOT NULL CHECK (status IN (0, 1)) DEFAULT 0
    )
    ''')
    conn.commit()
    conn.close()

initialize_db()

# Pydantic models
class TaskCreate(BaseModel):
    id: int
    title: str
    description: str
    time: str
    status: bool

class TaskUpdate(BaseModel):
    title: str = None
    description: str = None
    time: str = None
    status: bool = None

class Task(BaseModel):
    id: int
    title: str
    description: str
    time: str
    status: bool


# FastAPI Endpoints

# Add a simple route for the root URL
@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API. Check /docs for the API documentation."}


@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO tasks (id, title, description, time, status)
    VALUES (?, ?, ?, ?, ?)
    ''', (task.id, task.title, task.description, task.time, task.status))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return get_task(task_id)

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    task = cursor.fetchone()
    conn.close()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return dict(task)

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskUpdate):
    conn = get_db()
    cursor = conn.cursor()
    existing_task = cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    updated_task_data = {
        "title": task.title if task.title is not None else existing_task["title"],
        "description": task.description if task.description is not None else existing_task["description"],
        "time": task.time if task.time is not None else existing_task["time"],
        "status": int(task.status) if task.status is not None else existing_task["status"]
    }

    cursor.execute('''
    UPDATE tasks
    SET title = ?, description = ?, time = ?, status = ?
    WHERE id = ?
    ''', (updated_task_data["title"], updated_task_data["description"], updated_task_data["time"], updated_task_data["status"], task_id))
    conn.commit()
    conn.close()
    return get_task(task_id)

@app.delete("/tasks/{task_id}", response_model=dict)
def delete_task(task_id: int):
    conn = get_db()
    cursor = conn.cursor()
    task = cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return {"ok": True}

# @app.get("/tasks/", response_model=List[Task])
# def list_tasks():
#     conn = get_db()
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM tasks')
#     tasks = cursor.fetchall()
#     conn.close()
#     return [dict(task) for task in tasks]

@app.get("/tasks/", response_model=List[Task])
def list_task():
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
        conn.close()
        return [dict(task) for task in tasks]
    except Exception as e:
        print(f'Error: {e}')
        raise HTTPException(status_code=500, detail=f"Internal Server Error:{str(e)}")
