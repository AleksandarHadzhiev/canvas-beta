from fastapi import FastAPI, Depends
from .dependencies import get_token_header, get_query_token

app = FastAPI(dependencies=[Depends(get_query_token)])

@app.get('/')
async def root():
    return {'message': 'Canvas Beta'}