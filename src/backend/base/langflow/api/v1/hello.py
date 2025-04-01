from fastapi import APIRouter

# Build router with appropriate tag
router = APIRouter(prefix="/hello", tags=["Hello"])


@router.get("/")
async def hello_world():
    """
    Return a simple JSON response with "Hello World" message.
    
    Returns:
        dict: A dictionary with a greeting message
    """
    return {"message": "Hello World"}