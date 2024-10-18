"""Init the booting file for the FastAPI backend."""
from fastapi import FastAPI, Depends

from app.dependencies import  get_query_token
from app.db_conn import DBConnector
from app.routers import organization

app = FastAPI(dependencies=[Depends(get_query_token)])
db = DBConnector()
app.include_router(organization.router)
@app.on_event("startup")
def on_startup():
    """Initiate thd DB on startup"""
    db.create_db_and_tables()

@app.get('/')
async def root():
    """Basic endpoint.

    Returns:
        dict: contains the message which will be printed on the screen.
    """
    return {'message': 'Canvas Beta'}
