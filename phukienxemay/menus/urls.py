from django.urls import path
from .views import MenuViews, MenuViewDetails, MenuViewCreate, MenuViewUpdateDestroy, SubMenuViews, SubMenuViewDetails, \
    SubMenuViewCreate, SubMenuViewUpdateDestroy

urlpatterns = [
    path('menus', MenuViews.as_view()),
    path('menus/create', MenuViewCreate.as_view()),
    path('menus/<str:pk>/details', MenuViewDetails.as_view()),
    path('menus/<str:pk>', MenuViewUpdateDestroy.as_view()),
    #
    path('sub_menus', SubMenuViews.as_view()),
    path('sub_menus/create', SubMenuViewCreate.as_view()),
    path('sub_menus/<str:pk>/details', SubMenuViewDetails.as_view()),
    path('sub_menus/<str:pk>', SubMenuViewUpdateDestroy.as_view()),
]
