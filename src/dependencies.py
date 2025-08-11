from fastapi import Depends, Request
from src.service.cart_service import CartService
from src.service.user_service import UserService
from src.service.product_service import ProductService


def get_user_service(request: Request) -> UserService:
    return request.app.state.user_service


def get_product_service(request: Request) -> ProductService:
    return request.app.state.product_service


def get_cart_service(request: Request) -> CartService:
    return request.app.state.cart_service
