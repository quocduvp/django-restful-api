from django.urls import path
from .views import OrderViewList, OrderViewDetails, CheckOutView,VerifyDelivery

urlpatterns = [
    path('orders', OrderViewList.as_view()),
    path('orders/<str:id>', OrderViewDetails.as_view()),
    path('checkout', CheckOutView.as_view()),
    path('delivered/<str:id>', VerifyDelivery.as_view()),
]
