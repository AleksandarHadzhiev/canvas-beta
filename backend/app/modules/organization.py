from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import SQLModel, Field, Session, create_engine, select

class Organization(SQLModel, table = True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    owner: str
    