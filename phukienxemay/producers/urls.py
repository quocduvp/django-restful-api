from django.urls import path
from .views import ProducerViewCreate, ProducerViewList, ProducerViewDetails, ProducerViewDelete, ProducerViewUpdate
urlpatterns = [
    path('producers', ProducerViewList.as_view()),
    path('producers/create', ProducerViewCreate.as_view()),
    path('producers/<str:pk>/details', ProducerViewDetails.as_view()),
    path('producers/<str:pk>/edit', ProducerViewUpdate.as_view()),
    path('producers/<str:pk>/delete', ProducerViewDelete.as_view()),
]
