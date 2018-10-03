from django.urls import path
from .views import AccessoryViewList, AccessoryViewCreate, AccessoryViewDelete, AccessoryViewDetails, \
    AccessoryViewUpdate, RequireForViewList, RequireForViewCreate, RequireForViewDelete, RequireForViewUpdate, \
    ImageViewUpdate, ImageViewList, ImageViewDelete, ImageViewCreate, TagsViewCreate,TagsViewDelete, TagsViewUpdate,TagsViewList

urlpatterns = [
    path('accessories', AccessoryViewList.as_view()),
    path('accessories/create', AccessoryViewCreate.as_view()),
    path('accessories/<str:pk>/details', AccessoryViewDetails.as_view()),
    path('accessories/<str:pk>/edit', AccessoryViewUpdate.as_view()),
    path('accessories/<str:pk>/delete', AccessoryViewDelete.as_view()),
    #     Require for
    path('accessories/<str:accessory_id>/requires', RequireForViewList.as_view()),
    path('accessories/<str:accessory_id>/requires/create', RequireForViewCreate.as_view()),
    path('accessories/<str:accessory_id>/requires/<int:id>/edit', RequireForViewUpdate.as_view()),
    path('accessories/<str:accessory_id>/requires/<int:id>/delete', RequireForViewDelete.as_view()),
    #     Image
    path('accessories/<str:accessory_id>/images', ImageViewList.as_view()),
    path('accessories/<str:accessory_id>/images/create', ImageViewCreate.as_view()),
    path('accessories/<str:accessory_id>/images/<int:id>/edit', ImageViewUpdate.as_view()),
    path('accessories/<str:accessory_id>/images/<int:id>/delete', ImageViewDelete.as_view()),
    #     Tag
    path('accessories/<str:accessory_id>/tags', TagsViewList.as_view()),
    path('accessories/<str:accessory_id>/tags/create', TagsViewCreate.as_view()),
    path('accessories/<str:accessory_id>/tags/<int:id>/edit', TagsViewUpdate.as_view()),
    path('accessories/<str:accessory_id>/tags/<int:id>/delete', TagsViewDelete.as_view()),
]
