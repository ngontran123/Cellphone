from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from ..shemas.OrderSchema import OrderSchema
from ..services import OrderItemService
from rest_framework.routers import DefaultRouter
from ..serializers.OrderSerializer import OrderSerializer
from ..serializers.OrderItemSerializer import OrderItemSerializer


class OrderItemListView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        is_item, order_items = OrderItemService.get_order_items()
        if not is_item:
            return Response(order_items)
        serializer = OrderItemSerializer(order_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderItemDetailView(generics.GenericAPIView):
    def get(self, request, id, *args, **kwargs):
        is_item, order_item = OrderItemService.get_order_item_by_id((id))
        if not is_item:
            return Response(order_item)
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data, status=status.HTTP_200_OK)


