from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def read_items() -> None:
    """
    Retrieve items.
    """


@router.post("/")
async def update_item() -> None:
    """
    Update item.
    """
