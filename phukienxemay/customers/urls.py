from django.urls import path
from .views import CustomerViewsRegister, CustomerViewsResetPassword, CustomerViewsForgotPassword, \
    CustomerViewsVerifyForgotPassword, CustomerViewsProfile
from .serializers import CustomJWTSerializer
from rest_framework_jwt.views import ObtainJSONWebToken

urlpatterns = [
    path('register', CustomerViewsRegister.as_view()),
    path('login', ObtainJSONWebToken.as_view(serializer_class=CustomJWTSerializer)),
    path('reset_password', CustomerViewsResetPassword.as_view()),
    path('forgot_password', CustomerViewsForgotPassword.as_view()),
    path('verify_forgot_password', CustomerViewsVerifyForgotPassword.as_view()),
    path('profile', CustomerViewsProfile.as_view()),
]
