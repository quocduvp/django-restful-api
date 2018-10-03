from django.shortcuts import render
from rest_framework.generics import DestroyAPIView, ListCreateAPIView
from .serializers import ShoppingCartSerializer
from customers.serializers import CustomerSerializer
from accessories.serializers import AccessorySerializer
from accessories.models import accessory
from .models import Carts
from rest_framework import response, status, permissions
from phukienxemay.Authentication import DecodeToken
from django.contrib.auth.models import User


# Create your views here
#
# .Get list cart
class CartViewList(ListCreateAPIView):
    serializer_class = ShoppingCartSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = DecodeToken(request)
        try:
            return response.Response(list_cart(user['user_id']))
        except:
            return response.Response({'Message': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        user = DecodeToken(request)
        req = request.POST
        cart_details = list_cart(user['user_id'])
        item = list(filter(lambda x: str(x['accessory_id']) == str(req['accessory_id']), cart_details['carts']))
        if len(item) >= 1: #neu da co trong gi hang tien hanh cap nhat moi
            accessory_model = accessory.objects.get(id=req['accessory_id'])
            accessory_serializer = AccessorySerializer(accessory_model, many=False)
            # check sl ton kho co lon hon sl khong
            if int(accessory_serializer.data['qty']) >= int(req['qty']):
                cart = item[0]
                cart_model = Carts.objects.get(id = cart['id'])
                cart_serializer = ShoppingCartSerializer(cart_model,data=req, many=False)
                cart_serializer.is_valid(raise_exception=True)
                cart_serializer.save()
                return response.Response(list_cart(user['user_id']), status=status.HTTP_200_OK)
            else:
                return response.Response({'Message': 'Quantity not greater than quantity in stock.'})
        else: #neu chua co tien hanh them vao
            try:
                accessory_model = accessory.objects.get(id=req['accessory_id'])
                accessory_serializer = AccessorySerializer(accessory_model, many=False)
                # check sl ton kho co lon hon sl khong
                if int(accessory_serializer.data['qty']) >= int(req['qty']):
                    cart_serializer = ShoppingCartSerializer(data=req, many=False)
                    cart_serializer.is_valid(raise_exception=True)
                    cart_serializer.save()
                    return response.Response(list_cart(user['user_id']), status=status.HTTP_201_CREATED)
                else:
                    return response.Response({'Message': 'Quantity not greater than quantity in stock.'})
            except:
                return response.Response({'Message': 'Bad request.'}, status=status.HTTP_400_BAD_REQUEST)

class CartViewRemove(DestroyAPIView):
    serializer_class = ShoppingCartSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        user = DecodeToken(request)
        try:
            cart_id = self.kwargs['id']
            cart_model = Carts.objects.get(id=cart_id, user_id=user['user_id'])
            cart_model.delete()
            return response.Response(list_cart(user['user_id']), status=status.HTTP_200_OK)
        except:
            return response.Response({'Message': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

class CartViewRemoveAll(DestroyAPIView):
    serializer_class = ShoppingCartSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        user = DecodeToken(request)
        try:
            cart_model = Carts.objects.all().filter(user_id=user['user_id']).delete()
            return response.Response(list_cart(user['user_id']), status=status.HTTP_200_OK)
        except:
            return response.Response({'Message': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

# def list cart
def list_cart(user_id):
    customer_serializer = CustomerSerializer(User.objects.get(id=user_id), many=False)
    # loop list cart
    for dic in customer_serializer.data['carts']:
        dic['accessory_details'] = AccessorySerializer(accessory.objects.get(id=dic['accessory_id']), many=False).data
        # so tien
        dic['price'] = dic['qty'] * float(dic['accessory_details']['price'])
    return customer_serializer.data
