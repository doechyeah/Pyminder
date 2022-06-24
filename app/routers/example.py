from fastapi import APIRouter

router = APIRouter(
    prefix='/example',
    tags=['example']
) 

@router.get('/')
async def print():
    return {"message": "Hello, Example!"}