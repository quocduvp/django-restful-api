from django.shortcuts import render
from django.contrib.auth.models import User
from customers.serializers import CustomerSerializer
from .serializers import OrderItemSerializer, OrderSerializer
from .models import OrderItem, Orders
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status, response
from django.core.exceptions import ValidationError
from shopping_cart.views import list_cart
from accessories.models import accessory
from shopping_cart.models import Carts
from phukienxemay.Authentication import DecodeToken
from phukienxemay.settings import STRIPE_KEY
import stripe

stripe.api_key = STRIPE_KEY


# Create your views here.

class OrderViewList(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsAdminUser,)

    def get(self, request, *args, **kwargs):
        model_order = Orders.objects.all()
        serializer = self.serializer_class(model_order, many=True)
        for ser in serializer.data:
            user_model = CustomerSerializer(User.objects.get(id=ser['user_id']), many=False).data
            ser['user_details'] = user_model
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class OrderViewDetails(RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsAdminUser,)

    def get(self, request, *args, **kwargs):
        try:
            order_id = self.kwargs['id']
            model_order = Orders.objects.get(id=order_id)
            serializer = self.serializer_class(model_order, many=False).data
            user_model = CustomerSerializer(User.objects.get(id=serializer['user_id']), many=False).data
            serializer['user_details'] = user_model if user_model else None
            return response.Response(serializer, status=status.HTTP_200_OK)
        except ValidationError:
            return response.Response({'Message': '{} is not a valid UUID.'.format(self.kwargs['id'])},
                                     status=status.HTTP_400_BAD_REQUEST)
        except:
            return response.Response({'Message': 'Not found.'},
                                     status=status.HTTP_404_NOT_FOUND)


class CheckOutView(CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        req = request.POST  # card_number, cvc, exp_month, exp_year, address
        try:
            user = DecodeToken(request)
            user_cart = list_cart(user['user_id'])['carts']
            if len(user_cart) >= 1:
                # create token card
                tok_card = createToken(req)['id']
                # sum price from carts
                total_price = sum(cart['price'] for cart in user_cart)
                instance = {}
                instance['user_id'] = user['user_id']
                instance['total_price'] = total_price
                instance['address'] = req['address']
                order_serializer = self.serializer_class(data=instance)
                order_serializer.is_valid(raise_exception=True)
                order_serializer.save()
                #     payment
                charge = createCharge(source=tok_card, amount=round(total_price * 100),
                                      description="Charge for {}.".format(user['email']), address=req['address'])
                # check neu da thanh toan thanh cong
                if charge['paid'] == True:
                    # update table order
                    order_model = Orders.objects.get(id = order_serializer.data['id'])
                    order_model.is_pay = True
                    order_model.save()
                    # add Order Items
                    for cart in user_cart:
                        cart_instance = {}
                        cart_instance['accessory_id'] = cart['accessory_id']
                        cart_instance['order_id'] = order_serializer.data['id']
                        cart_instance['qty'] = cart['qty']
                        cart_instance['price'] = cart['price']
                        order_items_serializer = OrderItemSerializer(data=cart_instance)
                        order_items_serializer.is_valid(raise_exception=True)
                        order_items_serializer.save()
                        # update product
                        accessory_model = accessory.objects.get(id=cart['accessory_id'])
                        accessory_model.qty = int(accessory_model.qty) - int(cart['qty'])
                        accessory_model.save()
                        # Xoa gio hang
                        Carts.objects.filter(user_id = user['user_id']).delete()
                    return response.Response({'Message': 'Payment online is successful', 'details': charge},
                                             status=status.HTTP_200_OK)
                else:
                    return response.Response({'Message': 'Payment online is fails', 'details': charge},
                                             status=status.HTTP_200_OK)
            else:
                return response.Response({'Message': 'Shopping carts is null'}, status=status.HTTP_404_NOT_FOUND)
        except stripe.error.CardError:
            return response.Response({'Message': '{} Your card number is incorrect.'.format(req['card_number'])},
                                     status=status.HTTP_400_BAD_REQUEST)
        except:
            return response.Response({'Message': 'Bad request'.format(req['card_number'])},
                                     status=status.HTTP_400_BAD_REQUEST)

# Xac nhan da giao hang
class VerifyDelivery(UpdateAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsAdminUser,)

    def update(self, request, *args, **kwargs):
        try:
            order_id = self.kwargs['id']
            order_model = Orders.objects.get(id=order_id)
            order_model.is_delivery = True
            order_model.save()
            serializer = self.serializer_class(order_model, many=False)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return response.Response({'Message': 'Order is not found.'}, status=status.HTTP_404_NOT_FOUND)


def createToken(object):
    token = stripe.Token.create(
        card={
            'number': object['card_number'],
            'cvc': object['cvc'],
            'exp_month': int(object['exp_month']),
            'exp_year': int(object['exp_year'])
        }
    )
    return token


def createCharge(source, amount, description, address):
    charge = stripe.Charge.create(
        amount=amount,
        currency="usd",
        source=source,  # obtained with Stripe.js
        description=description,
        metadata={
            "address": address
        }
    )
    return charge
