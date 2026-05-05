from fastapi import APIRouter

from app.schemas.item import Item

router = APIRouter()


@router.get("/", response_model=list[Item])
async def list_items() -> list[Item]:
    return [
        Item(id=1, name="Example item", description="Replace this with real data."),
    ]
