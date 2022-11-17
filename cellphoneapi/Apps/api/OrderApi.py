import datetime

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
        is_order, orders = OrderService.get_order_by_status(8);
        if not is_order:
            return Response(orders)
        for order in orders:
            time_pass = (datetime.datetime.now()).replace(tzinfo=None)
            updated_time = order.updated_date.replace(tzinfo=None)
            diff = ((time_pass - updated_time).total_seconds()) / 60;
            if diff > 1:
                order_object = {'username': order.username, 'created_date': order.created_date,
                                'updated_date': order.updated_date, 'total_price': order.total_price,
                                'total_weight': order.total_price, 'status': 7, 'shipper_id': order.shipper_id.id,
                                'shipping_fee': order.shipping_fee}
                serializer = OrderSerializer(order, data=order_object)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
        is_order, order = OrderService.get_order_by_id(id)
        if not is_order:
            return Response(order)
        if role_id == 1:
            order_object = {'username': order.username, 'created_date': order.created_date,
                            'updated_date': order.updated_date, 'total_price': order.total_price,
                            'total_weight': order.total_price, 'status': 7, 'shipper_id': '',
                            'shipping_fee': order.shipping_fee}
            serializer = OrderSerializer(order, data=order_object)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            username = UserService.get_username_by_token(request)
            order_object = {'username': order.username, 'created_date': order.created_date,
                            'updated_date': order.updated_date, 'total_price': order.total_price,
                            'total_weight': order.total_price, 'status': 1, 'shipper_id': username,
                            'shipping_fee': order.shipping_fee}
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
                'updated_date': datetime.datetime.now(),
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


class OrderOverTimeView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):

        is_order, orders = OrderService.get_order_by_status(8);
        if not is_order:
            return Response(orders)
        for order in orders:
            time_pass = (datetime.datetime.now()).replace(tzinfo=None)
            updated_time = order.updated_date.replace(tzinfo=None)
            diff = ((time_pass - updated_time).total_seconds()) / 60;
            if diff > 1:
                order_object = {'username': order.username, 'created_date': order.created_date,
                                'updated_date': order.updated_date, 'total_price': order.total_price,
                                'total_weight': order.total_price, 'status': 7, 'shipper_id': order.shipper_id.id,
                                'shipping_fee': order.shipping_fee}
                serializer = OrderSerializer(order, data=order_object)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        is_order, orders = OrderService.get_order_by_status(8)
        if not is_order:
            return Response(order)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
