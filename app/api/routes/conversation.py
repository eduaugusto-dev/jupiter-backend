from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def conversation():

    return {
        "status": "conversation manager online"
    }