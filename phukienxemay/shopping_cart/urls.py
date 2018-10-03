from django.urls import path
from .views import CartViewList, CartViewRemove, CartViewRemoveAll

urlpatterns = [
    path('carts', CartViewList.as_view()),
    path('carts/<str:id>', CartViewRemove.as_view()),
    path('remove_carts', CartViewRemoveAll.as_view()),
]
