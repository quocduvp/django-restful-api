# Create your views here.
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .serializers import ProducerSerialer
from .models import Producer
from menus.PaginationCustom import StandardResultsSetPagination
from rest_framework import status, response


class ProducerViewList(ListAPIView):
    queryset = Producer.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ProducerSerialer
    pagination_class = StandardResultsSetPagination


class ProducerViewDetails(RetrieveAPIView):
    queryset = Producer.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ProducerSerialer


class ProducerViewCreate(CreateAPIView):
    queryset = Producer.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = ProducerSerialer


class ProducerViewUpdate(UpdateAPIView):
    queryset = Producer.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = ProducerSerialer


class ProducerViewDelete(DestroyAPIView):
    queryset = Producer.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = ProducerSerialer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return response.Response({'Message': "Deleted successful."}, status=status.HTTP_204_NO_CONTENT)
