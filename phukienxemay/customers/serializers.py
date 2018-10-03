from rest_framework import serializers
from django.contrib.auth import models
from rest_framework_jwt.views import JSONWebTokenSerializer
from shopping_cart.serializers import ShoppingCartSerializer
from orders.serializers import OrderSerializer
#
from django.contrib.auth import authenticate, get_user_model
from rest_framework_jwt.settings import api_settings
from django.utils.translation import ugettext as _
User = get_user_model()
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class CustomerSerializer(serializers.ModelSerializer):
    carts = ShoppingCartSerializer(read_only=True, many=True)
    orders = OrderSerializer(read_only=True, many=True)
    class Meta:
        model = models.User
        fields = ('id', 'username', 'password', 'email', 'is_staff', 'first_name', 'last_name', 'date_joined', 'last_login', 'carts', 'orders')
        extra_kwargs = {'password': {'write_only': True}}


# Login with email
class CustomJWTSerializer(JSONWebTokenSerializer):
    username_field = 'email'  # email or username

    def validate(self, attrs):

        password = attrs.get("password")
        user_obj = User.objects.filter(email=attrs.get("email")).first() or User.objects.filter(
            username=attrs.get("username")).first()
        if user_obj is not None:
            credentials = {
                'username': user_obj.username,
                'password': password
            }
            if all(credentials.values()):
                user = authenticate(**credentials)
                if user:
                    if not user.is_active:
                        msg = _('User account is disabled.')
                        raise serializers.ValidationError(msg)

                    payload = jwt_payload_handler(user)

                    return {
                        'token': jwt_encode_handler(payload),
                        'user': user
                    }
                else:
                    msg = _('Unable to log in with provided credentials.')
                    raise serializers.ValidationError(msg)

            else:
                msg = _('Must include "{username_field}" and "password".')
                msg = msg.format(username_field=self.username_field)
                raise serializers.ValidationError(msg)

        else:
            msg = _('Account with this email/username does not exists')
            raise serializers.ValidationError(msg)
