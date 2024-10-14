"""Init the booting file for the FastAPI backend."""
from fastapi import FastAPI, Depends
from .dependencies import  get_query_token

app = FastAPI(dependencies=[Depends(get_query_token)])

@app.get('/')
async def root():
    """Basic endpoint.

    Returns:
        dict: contains the message which will be printed on the screen.
    """
    return {'message': 'Canvas Beta'}
