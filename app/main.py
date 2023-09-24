from fastapi import FastAPI, Depends, Request, status
from sqlalchemy.orm import Session

from db import models
from . import schemas, crud
from .db import SessionLocal, engine
from starlette.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.exception_handler(RequestValidationError)
async def handler(request:Request, exc:RequestValidationError):
    print(exc)
    return JSONResponse(content={}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

@app.get("/")
def Hello():
    return {"Hello":"World!"}

@app.get("/todos", response_model=list[schemas.Todo])
def get_todos(db: Session = Depends(get_db)):
    todos = crud.get_todos(db)

@app.post("/todo/", response_model=schemas.Todo)
async def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, todo=todo)

# @app.get("/todos")
# def read_todo():
#     todos = session.query(Todo).all()
#     return todos

# @app.post("/todos/", response_model=model.Todo)
# def create_todo(todo: model.Todo, db: session):
#     return crud.create_todo(db=db, todo=todo)

