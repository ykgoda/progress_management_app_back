from pydantic import BaseModel, constr
from datetime import datetime

# Todo
class TodoBase(BaseModel):
    title: str
    description: constr(max_length=200)
    dueDate: str
    createBy: str
    progress: int
    genre: str
    memos: list[dict]
    isShowDetails: bool

    class Config:
        orm_mode = True

class Todo(TodoBase):
    id: str
    createAt: datetime = datetime.now()
    updateAt: datetime = None

class TodoCreate(TodoBase):
    pass

# Memo
class MemoBase(BaseModel):
    content: constr(max_length=200)
    createBy: str
    isEdited: bool

    class Config:
        orm_mode = True

class Memo(MemoBase):
    id: int
    createAt: datetime

class MemoCreate(MemoBase):
    pass