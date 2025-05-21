from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.cart import schemas, services
from app.core.database import get_db
from app.user.dependencies import get_current_user
from app.user.models import User

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.post(
    "/items/",
    response_model=schemas.CartItemRead,
    summary="Add item to cart",
    description="Adds a movie to the authenticated user's cart."
)
def add_item_to_cart(
    item: schemas.CartItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return services.add_item_to_cart(db, current_user, item.movie_id)

@router.delete(
    "/items/{movie_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Remove item from cart",
    description="Removes a specific movie from the authenticated user's cart."
)
def remove_item_from_cart(
    movie_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    services.remove_item_from_cart(db, current_user, movie_id)
    return

@router.get(
    "/",
    response_model=schemas.CartRead,
    summary="Get cart contents",
    description="Retrieves the current contents of the authenticated user's cart."
)
def get_cart(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return services.get_cart(db, current_user)

@router.post(
    "/checkout",
    status_code=status.HTTP_200_OK,
    summary="Checkout cart",
    description="Processes the purchase of all items in the user's cart."
)
def checkout_cart(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    services.checkout_cart(db, current_user)
    return {"message": "Purchase successful"}

@router.delete(
    "/clear",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Clear cart",
    description="Removes all items from the authenticated user's cart."
)
def clear_cart(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    services.clear_cart(db, current_user)
    return
