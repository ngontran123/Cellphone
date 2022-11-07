from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from ..shemas.OrderSchema import OrderSchema
from ..services import OrderService, UserService
from rest_framework.routers import DefaultRouter
from ..serializers.OrderSerializer import OrderSerializer
from rest_framework.exceptions import AuthenticationFailed


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        role_id = UserService.get_role_by_token(request)
        if role_id != 1:
            raise AuthenticationFailed("You dont have the right to access this feature.")
        is_order, orders = OrderService.get_all_order()
        if not is_order:
            return Response(orders)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderDetailListView(generics.GenericAPIView):
    serializer_class = OrderSerializer

    def get(self, request, id, *args, **kwargs):
        role_id = UserService.get_role_by_token(request)
        if role_id != 1 and role_id != 2:
            raise AuthenticationFailed('You dont have the right to access this feature.')
        is_order, order = OrderService.get_order_by_id(id)
        if not is_order:
            return Response(order)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id, *args, **kwargs):
        role_id = UserService.get_role_by_token(request)
        if role_id != 1 and role_id != 3:
            raise AuthenticationFailed('You dont have the right to access this feature.')
        order_object = request.data
        is_order, order = OrderService.get_order_by_id(id)
        if not is_order:
            return Response(order)
        if role_id == 1:
            order_object['shipper_id'] = ''
            order_object['status'] = 5
            serializer = OrderSerializer(order, data=order_object)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            username = UserService.get_username_by_token(request)
            order_object['shipper_id'] = username
            order_object['status'] = 1
            serializer = OrderSerializer(order, data=order_object)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, *args, **kwargs):
        role_id = UserService.get_role_by_token(request)
        if role_id != 1 and role_id != 3:
            raise AuthenticationFailed('You dont have the right to access this feature')
        is_order, order = OrderService.get_order_by_id(id)
        order_object = request.data
        if role_id == 1:
            updated_object = {
                'username': order.username,
                'created_date': order.created_date,
                'updated_date': order.updated_date,
                'total_price': order.total_price,
                'total_weight': order.total_weight,
                'shipping_fee': order.shipping_fee,
                'shipper_id': order_object['shipper_id'],
                'status': order_object['status']
            }
            serializer = OrderSerializer(order, data=updated_object)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            username = UserService.get_username_by_token(request)
            updated_object = {
                'username': order.username,
                'created_date': order.created_date,
                'updated_date': order.updated_date,
                'total_price': order.total_price,
                'total_weight': order.total_weight,
                'shipping_fee': order.shipping_fee,
                'shipper_id': username,
                'status': order_object['status']
            }
            serializer = OrderSerializer(order, data=updated_object)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_200_OK)




