from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import motorbike
from .serializers import MotorbikeSerializer
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import response, status
from menus.PaginationCustom import StandardResultsSetPagination


# Create your views here.
class MotorbikeViewList(ListAPIView):
    queryset = motorbike.objects.all()
    serializer_class = MotorbikeSerializer
    permission_classes = (AllowAny,)
    pagination_class = StandardResultsSetPagination


class MotorbikeViewDetails(RetrieveAPIView):
    queryset = motorbike.objects.all()
    serializer_class = MotorbikeSerializer
    permission_classes = (AllowAny,)


class MotorbikeViewCreate(CreateAPIView):
    queryset = motorbike.objects.all()
    serializer_class = MotorbikeSerializer
    permission_classes = (IsAdminUser,)


class MotorbikeViewEdit(UpdateAPIView):
    queryset = motorbike.objects.all()
    serializer_class = MotorbikeSerializer
    permission_classes = (IsAdminUser,)


class MotorbikeViewDelete(DestroyAPIView):
    queryset = motorbike.objects.all()
    serializer_class = MotorbikeSerializer
    permission_classes = (IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return response.Response({'Message': 'Deleted successful.'}, status=status.HTTP_204_NO_CONTENT)
