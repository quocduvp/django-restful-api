from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from .models import accessory, tag, image, require_for
from .serializers import AccessorySerializer, ImageSerializer, RequiredForSerializer, TagSerializer
from menus.PaginationCustom import StandardResultsSetPagination
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import status, response
from django.core.exceptions import ValidationError


# Create your views here.

class AccessoryViewList(ListAPIView):
    queryset = accessory.objects.all()
    serializer_class = AccessorySerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = (AllowAny,)


class AccessoryViewDetails(RetrieveAPIView):
    queryset = accessory.objects.all()
    serializer_class = AccessorySerializer
    permission_classes = (AllowAny,)


class AccessoryViewCreate(CreateAPIView):
    queryset = accessory.objects.all()
    serializer_class = AccessorySerializer
    permission_classes = (IsAdminUser,)


class AccessoryViewUpdate(UpdateAPIView):
    queryset = accessory.objects.all()
    serializer_class = AccessorySerializer
    permission_classes = (IsAdminUser,)


class AccessoryViewDelete(DestroyAPIView):
    queryset = accessory.objects.all()
    serializer_class = AccessorySerializer
    permission_classes = (IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return response.Response({'Message': "Deleted successful."}, status=status.HTTP_204_NO_CONTENT)


# Require for
class RequireForViewList(ListAPIView):
    serializer_class = RequiredForSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            model = require_for.objects.all().filter(accessory_id=self.kwargs['accessory_id'])
            serializer = self.serializer_class(model, many=True)
            return response.Response(serializer.data)
        except:
            return response.Response({'Message': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

class RequireForViewCreate(CreateAPIView):
    serializer_class = RequiredForSerializer
    permission_classes = (IsAdminUser,)

    def post(self, request, *args, **kwargs):
        self.request.POST._mutable = True
        request.data["accessory_id"] = self.kwargs["accessory_id"]
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class RequireForViewDelete(DestroyAPIView):
    serializer_class = RequiredForSerializer
    permission_classes = (IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        try:
            model = require_for.objects.get(accessory_id=self.kwargs['accessory_id'], id=self.kwargs['id'])
            model.delete()
            return response.Response({'Message': 'Delete successful.'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return response.Response({'Message': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class RequireForViewUpdate(UpdateAPIView):
    serializer_class = RequiredForSerializer
    permission_classes = (IsAdminUser,)

    def update(self, request, *args, **kwargs):
        try:
            self.request.POST._mutable = True
            accessory_id = self.kwargs["accessory_id"]
            obj = require_for.objects.get(accessory_id=accessory_id, id=self.kwargs["id"])
            request.data["accessory_id"] = self.kwargs["accessory_id"]
            serializer = self.serializer_class(obj, data=request.data, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            if getattr(obj, '_prefetched_objects_cache', None):
                obj._prefetched_objects_cache = {}
            return response.Response(serializer.data)
        except ValidationError:
            return response.Response({'Message': '{} UUID is valid'.format(self.kwargs["accessory_id"])},
                                     status=status.HTTP_400_BAD_REQUEST)
        except:
            return response.Response({'Message': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


# Image
class ImageViewList(ListAPIView):
    serializer_class = ImageSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            model = image.objects.all().filter(accessory_id=self.kwargs['accessory_id'])
            serializer = self.serializer_class(model, many=True)
            return response.Response(serializer.data)
        except:
            return response.Response({'Message': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class ImageViewCreate(CreateAPIView):
    serializer_class = ImageSerializer
    permission_classes = (IsAdminUser,)

    def post(self, request, *args, **kwargs):
        self.request.POST._mutable = True
        request.data["accessory_id"] = self.kwargs["accessory_id"]
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ImageViewDelete(DestroyAPIView):
    serializer_class = ImageSerializer
    permission_classes = (IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        try:
            model = image.objects.get(accessory_id=self.kwargs['accessory_id'], id=self.kwargs['id'])
            model.delete()
            return response.Response({'Message': 'Delete successful.'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return response.Response({'Message': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class ImageViewUpdate(UpdateAPIView):
    serializer_class = ImageSerializer
    permission_classes = (IsAdminUser,)

    def update(self, request, *args, **kwargs):
        try:
            self.request.POST._mutable = True
            accessory_id = self.kwargs["accessory_id"]
            obj = image.objects.get(accessory_id=accessory_id, id=self.kwargs["id"])
            request.data["accessory_id"] = self.kwargs["accessory_id"]
            serializer = self.serializer_class(obj, data=request.data, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            if getattr(obj, '_prefetched_objects_cache', None):
                obj._prefetched_objects_cache = {}
            return response.Response(serializer.data)
        except ValidationError:
            return response.Response({'Message': '{} UUID is valid'.format(self.kwargs["accessory_id"])},
                                     status=status.HTTP_400_BAD_REQUEST)
        except:
            return response.Response({'Message': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

# tags
class TagsViewList(ListAPIView):
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            model = tag.objects.all().filter(accessory_id=self.kwargs['accessory_id'])
            serializer = self.serializer_class(model, many=True)
            return response.Response(serializer.data)
        except:
            return response.Response({'Message': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

class TagsViewCreate(CreateAPIView):
    serializer_class = TagSerializer
    permission_classes = (IsAdminUser,)

    def post(self, request, *args, **kwargs):
        self.request.POST._mutable = True
        request.data["accessory_id"] = self.kwargs["accessory_id"]
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TagsViewDelete(DestroyAPIView):
    serializer_class = TagSerializer
    permission_classes = (IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        try:
            model = tag.objects.get(accessory_id=self.kwargs['accessory_id'], id=self.kwargs['id'])
            model.delete()
            return response.Response({'Message': 'Delete successful.'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return response.Response({'Message': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class TagsViewUpdate(UpdateAPIView):
    serializer_class = TagSerializer
    permission_classes = (IsAdminUser,)

    def update(self, request, *args, **kwargs):
        try:
            self.request.POST._mutable = True
            accessory_id = self.kwargs["accessory_id"]
            obj = tag.objects.get(accessory_id=accessory_id, id=self.kwargs["id"])
            request.data["accessory_id"] = self.kwargs["accessory_id"]
            serializer = self.serializer_class(obj, data=request.data, many=False)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            if getattr(obj, '_prefetched_objects_cache', None):
                obj._prefetched_objects_cache = {}
            return response.Response(serializer.data)
        except ValidationError:
            return response.Response({'Message': '{} UUID is valid'.format(self.kwargs["accessory_id"])},
                                     status=status.HTTP_400_BAD_REQUEST)
        except:
            return response.Response({'Message': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


