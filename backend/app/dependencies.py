from typing import Annotated

from fastapi import Header, HTTPException


async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != 'secret-token':
        raise HTTPException(status_code=401, detail='Invalid token')


async def get_query_token(token: str):
    if token != 'secret-token':
        raise HTTPException(status_code=401, detail='Invalid token')