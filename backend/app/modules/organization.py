"""Organization."""
from sqlmodel import SQLModel, Field

class Organization(SQLModel, table = True):
    """Organization model representing the organizations table."""
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    owner: str
    