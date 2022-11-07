from rest_framework.response import Response
from rest_framework import generics, status
from ..services import OrderItemService
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

    def delete(self,request,id,*args,**kwargs):
        is_item,order_item=OrderItemService.get_order_item_by_id(id)
        if not is_item:
            return Response(order_item)
        order_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderItemByOrderDetailView(generics.GenericAPIView):
    def get(self, request, order_id, *args, **kwargs):
        is_item, order_items = OrderItemService.get_order_item_by_order_id(order_id)
        if not is_item:
            return Response(order_items)
        serializer = OrderItemSerializer(order_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

