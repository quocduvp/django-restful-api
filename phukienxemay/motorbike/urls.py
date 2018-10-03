from django.urls import path
from .views import MotorbikeViewList, MotorbikeViewCreate, MotorbikeViewDelete, MotorbikeViewDetails, MotorbikeViewEdit

urlpatterns = [
    path('motorbikes', MotorbikeViewList.as_view()),
    path('motorbikes/create', MotorbikeViewCreate.as_view()),
    path('motorbikes/<str:pk>/details', MotorbikeViewDetails.as_view()),
    path('motorbikes/<str:pk>/edit', MotorbikeViewEdit.as_view()),
    path('motorbikes/<str:pk>/delete', MotorbikeViewDelete.as_view()),
]
