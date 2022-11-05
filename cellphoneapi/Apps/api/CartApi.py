import datetime

from rest_framework.response import Response
from rest_framework import generics, status
from ..serializers.CartSerializer import CartSerializer
from ..services import CartService, UserService, CartItemsService,OrderService
from rest_framework.routers import DefaultRouter
from ..serializers.OrderSerializer import OrderSerializer
from ..serializers.OrderItemSerializer import OrderItemSerializer

router = DefaultRouter()


class CartList(generics.ListAPIView):
    serializer_class = CartSerializer

    def get(self, *args, **kwargs):
        is_carts, carts = CartService.get_all_cart()
        if not is_carts:
            return Response(carts)
        cart_serializers = CartSerializer(carts, many=True)
        return Response(cart_serializers.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        cart_object = request.data
        username = UserService.get_username_by_token(request)
        new_cart = CartService.mapping_cart(cart_object, username)
        is_cart, cart_exist = CartService.get_cart_by_username(username)
        if is_cart:
            return Response('Cart has existed')
        serializer = CartSerializer(data=new_cart)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartListDetail(generics.ListAPIView):
    serializer_class = CartSerializer

    def get(self, request, id, *args, **kwargs):
        is_cart, cart = CartService.get_cart_by_id(id)
        if not is_cart:
            return Response(cart)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        try:
            id = self.kwargs['id']
            is_cart, cart = CartService.get_cart_by_id(id)
            if not is_cart:
                return Response(cart)
            serializer = CartSerializer(cart, data=request.data)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': 'Cannot get field from request'})

    def delete(self, request, *args, **kwargs):
        try:
            username = UserService.get_username_by_token(request)
            is_cart, cart = CartService.get_cart_by_username(username)
            if not is_cart:
                return Response(cart)
            is_cart_item, cart_items = CartItemsService.get_cart_items_by_cart_id(cart.id)
            if not is_cart_item:
                return Response(cart_items)
            order_object = {
                'username': username,
                'created_date': datetime.datetime.utcnow(),
                'updated_date': datetime.datetime.utcnow(),
                'total_price': cart.total_price,
                'total_weight': cart.total_weight,
                'status': 2
            }
            order_serializer = OrderSerializer(data=order_object)
            if order_serializer.is_valid():
                order_serializer.save()
            else:
                return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            is_order,order=OrderService.get_order_by_username(username)
            if not is_order:
                return Response(order)
            for item in cart_items:
                order_items_object = {
                    'pd': item.pd,
                    'order':order.id,
                    'price':item.price,
                    'weight':item.weight,
                    'product_name':item.product_name,
                    'quantity':item.quantity
                }
                order_item_serializer=OrderItemSerializer(data=order_items_object)
                if order_item_serializer.is_valid():
                    order_item_serializer.save()
                else:
                    return Response(order_item_serializer.errors,status=status.HTTP_200_OK)
            cart.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': 'Cannot get field from request'})


class CartByUserName(generics.ListAPIView):
    def get(self, request, username, *args, **kwargs):
        is_cart, cart = CartService.get_cart_by_username(username)
        if not is_cart:
            return Response(cart)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
