from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from ..shemas.OrderSchema import OrderSchema
from ..services import OrderService
from rest_framework.routers import DefaultRouter
from ..serializers.OrderSerializer import OrderSerializer


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get(self, *args, **kwargs):
        is_order, orders = OrderService.get_all_order()
        if not is_order:
            return Response(orders)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderDetailListView(generics.GenericAPIView):
    def get(self, request, id, *args, **kwargs):
        is_order, order = OrderService.get_order_by_id(id)
        if not is_order:
            return Response(order)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
