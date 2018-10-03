from .serializers import MenuSerializer, SubMenuSerializer
from .models import Menu, SubMenu
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView, UpdateAPIView, \
    DestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from .PaginationCustom import StandardResultsSetPagination
from rest_framework.response import Response
from rest_framework import status


# menu.

class MenuViews(ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (AllowAny,)
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MenuViewDetails(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (AllowAny,)


class MenuViewCreate(CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsAdminUser,)


class MenuViewUpdateDestroy(DestroyAPIView, UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"Success": "Deleted successful."}, status=status.HTTP_204_NO_CONTENT)


#  submenu.

class SubMenuViews(ListAPIView):
    queryset = SubMenu.objects.all()
    serializer_class = SubMenuSerializer
    permission_classes = (AllowAny,)
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SubMenuViewDetails(RetrieveUpdateDestroyAPIView):
    queryset = SubMenu.objects.all()
    serializer_class = SubMenuSerializer
    permission_classes = (AllowAny,)


class SubMenuViewCreate(CreateAPIView):
    queryset = SubMenu.objects.all()
    serializer_class = SubMenuSerializer
    permission_classes = (IsAdminUser,)


class SubMenuViewUpdateDestroy(DestroyAPIView, UpdateAPIView):
    queryset = SubMenu.objects.all()
    serializer_class = SubMenuSerializer
    permission_classes = (IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"Success": "Deleted successful."}, status=status.HTTP_204_NO_CONTENT)
