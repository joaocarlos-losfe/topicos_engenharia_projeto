from fastapi import APIRouter

router = APIRouter()

@router.get("/auth", tags=["auth"])
async def auth():
    pass
