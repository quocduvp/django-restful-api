from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView
from .serializers import CustomerSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.contrib.auth import models
from rest_framework import status, response
from phukienxemay.hash import hash_password, check_hash_password, encode_text, decode_text
from phukienxemay.Authentication import DecodeToken
from phukienxemay.SendMail import SendMail


# Create your views here.
class CustomerViewsRegister(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CustomerSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            req = request.POST
            if req['password'] == req['confirm_password']:
                instance = {}
                instance['username'] = req['username']
                instance['email'] = req['email']
                instance['password'] = hash_password(req['password'])
                serializer = self.serializer_class(data=instance)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                return response.Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return response.Response({'Message': 'Password do not exist.'})
        except:
            return response.Response({'Message': 'Bad request.'},
                                     status=status.HTTP_400_BAD_REQUEST)


# update new password
class CustomerViewsResetPassword(UpdateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        decode = DecodeToken(request)
        try:
            if request.POST['password'] == request.POST['confirm_password']:
                instance = models.User.objects.get(id=decode['user_id'])
                req = {}
                req['username'] = decode['username']
                req['password'] = hash_password(request.POST['password'])
                serializer = self.serializer_class(instance, many=False)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return response.Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return response.Response({'Message': 'Confirm password do not exits.'},
                                         status=status.HTTP_400_BAD_REQUEST)
        except:
            return response.Response({'Message': 'Form is null.'}, status=
            status.HTTP_400_BAD_REQUEST)


#
class CustomerViewsForgotPassword(CreateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            send = SendMail()
            send.send_from = request.POST['email']
            send.send_to = request.POST['email']
            send.subject = "Forgot password!"
            token = encode_text(request.POST['email'])
            send.content = "Redirect to forgot password: https://example.com?token={}".format(token)
            if send.send_mail() == 202:
                return response.Response(
                    {'Message': 'Has sent a verification code to your email, please check your email'},
                    status=status.HTTP_202_ACCEPTED)
            else:
                return response.Response({'Message': 'Bad request.'},
                                         status=status.HTTP_400_BAD_REQUEST)
        except:
            return response.Response({'Message': 'Form is null.'}, status=
            status.HTTP_400_BAD_REQUEST)


class CustomerViewsVerifyForgotPassword(UpdateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = (AllowAny,)

    def update(self, request, *args, **kwargs):
        try:
            req = request.POST
            if req['password'] == req['confirm_password']:
                decode = decode_text(req['token'])
                instance = models.User.objects.get(email=decode['text'], username=req['username'])
                obj = {}
                obj['username'] = req['username']
                obj['password'] = hash_password(req['password'])
                serializer = self.serializer_class(instance, data=obj, many=False)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return response.Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return response.Response({'Message': 'Bad request.'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return response.Response({'Message': 'Form is null.'}, status=
            status.HTTP_400_BAD_REQUEST)


# get profile
class CustomerViewsProfile(RetrieveAPIView):
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = DecodeToken(request)
        try:
            instance = models.User.objects.get(id=user['user_id'])
            serializer = self.serializer_class(instance, many=False)
            return response.Response(serializer.data)
        except:
            return response.Response({'Message': 'Error.'}, status=
            status.HTTP_400_BAD_REQUEST)