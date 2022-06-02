from fastapi import APIRouter
from typing import Optional
from app import database,utils

router = APIRouter()


@router.get("/v1/quotes")
async def get_random_quote():
    count = await database.count_quotes()
    count = utils.random_number(count)
    return await database.get_randomquote( str(count) )

@router.get("/v1/quotes/{author_name}")
async def get_author_quote(author_name:str, limit: Optional[int]=1):
    return await database.get_quote(author_name, str(limit) )
