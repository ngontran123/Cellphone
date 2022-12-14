from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import generics, status
from ..serializers.OrderStatusSerializer import OrderStatusSerializer
from ..services import OrderStatusService, UserService


class OrderStatusListView(generics.ListAPIView):
    serializer_class = OrderStatusSerializer

    def get(self, request, *args, **kwargs):

        is_status, ord_status = OrderStatusService.get_all_order_status()
        if not is_status:
            return Response(ord_status)
        serializer = OrderStatusSerializer(ord_status, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        role_id = UserService.get_role_by_token(request)
        if role_id != 1:
            raise AuthenticationFailed('You dont have the right to access this feature.')
        object = request.data
        status_name = object['status_name']
        is_status, status_name = OrderStatusService.get_order_status_by_name(status_name)
        if is_status:
            return Response('This status has existed in your database.')
        serializer = OrderStatusSerializer(data=object)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderStatusByName(generics.GenericAPIView):
    serializer_class = OrderStatusSerializer

    def get(self, request, name, *args, **kwargs):
        is_order, order = OrderStatusService.get_order_status_by_name(name)
        if not is_order:
            return Response(order)
        serializer = OrderStatusSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        role_id = UserService.get_role_by_token(request)
        if role_id != 1:
            raise AuthenticationFailed('You dont have the right to access this feature.')
        object = request.data
        status_name = object['status_name']
        is_order, order = OrderStatusService.get_order_status_by_name(status_name)
        if not is_order:
            return Response(order)
        serializer = OrderStatusSerializer(order, data=object)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, name, *args, **kwargs):
        role_id = UserService.get_role_by_token(request)
        if role_id != 1:
            raise AuthenticationFailed('You dont have the right to access this feature.')
        is_order, order = OrderStatusService.get_order_status_by_name(name)
        if not is_order:
            return Response(order)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
