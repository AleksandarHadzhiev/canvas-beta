"""Init the dependencies needed to make API calls."""
from typing import Annotated


from fastapi import Header, HTTPException

async def get_token_header(x_token: Annotated[str, Header()]):
    """Get the token header.

    Args:
        x_token (Annotated[str, Header): _description_

    Raises:
        HTTPException: _description_
    """
    if x_token != 'secret-token':
        raise HTTPException(status_code=401, detail='Invalid token')


async def get_query_token(token: str):
    """Get the query token.

    Args:
        token (str): _description_

    Raises:
        HTTPException: _description_
    """
    if token != 'secret-token':
        raise HTTPException(status_code=401, detail='Invalid token')
