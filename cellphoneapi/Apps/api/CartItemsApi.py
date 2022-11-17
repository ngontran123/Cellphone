import datetime

from rest_framework.response import Response
from rest_framework import generics, status
from ..serializers.CartItemSerializer import CartItemSerializer, CartSerializer
from ..services import CartItemsService, ProductService, CartService, UserService
from rest_framework.routers import DefaultRouter


class CartItemList(generics.ListAPIView):
    serializer_class = CartItemSerializer

    def get(self, request,*args, **kwargs):

        is_cart_item, cart_item = CartItemsService.get_all_cart_items()
        if not is_cart_item:
            return Response(cart_item)
        serializer = CartItemSerializer(cart_item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        cart_item_object = request.data
        username = UserService.get_username_by_token(request)
        is_cart, cart = CartService.get_cart_by_username(username)
        is_product, product = ProductService.get_product_by_id(cart_item_object['pd'])
        if not is_product:
            return Response(product)
        if not is_cart:
            return Response(cart)
        price = product.price
        weight = product.weight
        quantity = int(cart_item_object['quantity'])
        total_price = int(cart.total_price) + (int(price) * int(quantity))
        total_weight = int(cart.total_weight) + (int(weight) * int(quantity))
        car_obj = {
            'username': cart.username,
            'created_date': cart.created_date,
            'updated_date': datetime.datetime.utcnow(),
            'total_price': total_price,
            'total_weight': total_weight
        }
        cart_serializer = CartSerializer(cart, data=car_obj)
        if cart_serializer.is_valid():
            cart_serializer.save()
        else:
            return Response('message:Cannot update cart.')
        is_exist_pd, pd_existed = CartItemsService.check_product_exists_in_cart(cart.id, cart_item_object['pd'])
        if is_exist_pd:
            quantity = cart_item_object['quantity'] + pd_existed.quantity
            cart_item_update = {
                'cart': cart.id,
                'pd': pd_existed.pd.id,
                'price': pd_existed.price,
                'weight': pd_existed.weight,
                'product_name': pd_existed.product_name,
                'quantity': quantity
            }
            update_cart_item_serializer = CartItemSerializer(pd_existed, data=cart_item_update)
            if update_cart_item_serializer.is_valid():
                update_cart_item_serializer.save()
                return Response(update_cart_item_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(update_cart_item_serializer.errors)
        else:
            new_cart_item = CartItemsService.add_cart_items(cart_item_object, cart.id)
            serializer = CartItemSerializer(data=new_cart_item)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartItemIdDetail(generics.ListAPIView):
    serializer_class = CartItemSerializer

    def get(self, request, id, *args, **kwargs):
        username = UserService.get_username_by_token(request)
        is_cart_item, cart_item = CartItemsService.get_cart_items_by_id(id)
        if not is_cart_item:
            return Response(cart_item)
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id, *args, **kwargs):
        username = UserService.get_username_by_token(request)
        is_cart_item, cart_item = CartItemsService.get_cart_items_by_id(id)
        if not is_cart_item:
            return Response(cart_item)
        is_cart, cart = CartService.get_cart_by_username(username)
        if not is_cart:
            return Response(cart)
        cart_update = {
            'username': username,
            'created_date': cart.created_date,
            'updated_date': datetime.datetime.utcnow(),
            'total_price': int(cart.total_price) - int(cart_item.price * cart_item.quantity),
            'total_weight': int(cart.total_weight) - int(cart_item.weight * cart_item.quantity)
        }
        cart_serializer = CartSerializer(cart, data=cart_update)
        if cart_serializer.is_valid():
            cart_serializer.save()
        else:
            return Response(cart_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if not is_cart_item:
            return Response(cart_item)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id, *args, **kwargs):
        username = UserService.get_username_by_token(request)
        data_object = request.data
        is_cart_item, cart_items = CartItemsService.get_cart_items_by_id(id)
        if not is_cart_item:
            return Response(cart_items)
        is_cart, cart = CartService.get_cart_by_id(cart_items.cart.id)
        if not is_cart:
            return Response(cart)
        is_product, product = ProductService.get_product_by_id(cart_items.pd.id)
        if not is_product:
            return Response(product)
        price = int(product.price)
        weight = int(product.weight)
        total_price = int(cart.total_price) - (int(cart_items.price) * int(cart_items.quantity)) + (
                    price * data_object['quantity'])
        total_weight = int(cart.total_weight) - (int(cart_items.weight) * int(cart_items.quantity)) + (
                    weight * int(data_object['quantity']))
        cart_update_object = {
            'username': cart.username,
            'created_date': cart.created_date,
            'updated_date': datetime.datetime.utcnow(),
            'total_price': total_price,
            'total_weight': total_weight
        }
        cart_serializer = CartSerializer(cart, data=cart_update_object)
        if cart_serializer.is_valid():
            cart_serializer.save()
        else:
            return Response(cart_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        cart_items_object = {
            'cart': cart.id,
            'pd': product.id,
            'price': product.price,
            'weight': product.weight,
            'product_name': product.name,
            'quantity': data_object['quantity']
        }
        serializer = CartItemSerializer(cart_items, data=cart_items_object)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartItemByCartIdDetail(generics.ListAPIView):
    def get(self, request, cart_id, *args, **kwargs):
        is_cart_item, cart_item = CartItemsService.get_cart_items_by_cart_id(cart_id)
        if not is_cart_item:
            return Response(cart_item)
        serializer = CartItemSerializer(cart_item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

