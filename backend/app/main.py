"""Init the booting file for the FastAPI backend."""
from fastapi import FastAPI, Depends
from .dependencies import  get_query_token
from .db_conn import DBConnector

app = FastAPI(dependencies=[Depends(get_query_token)])
@app.on_event("startup")
def on_startup():
    db = DBConnector()
    db.create_db_and_tables()
@app.get('/')
async def root():
    """Basic endpoint.

    Returns:
        dict: contains the message which will be printed on the screen.
    """
    return {'message': 'Canvas Beta'}
