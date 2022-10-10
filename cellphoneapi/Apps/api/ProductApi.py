from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from ..serializers.ProductSerializer import ProductSerializer
from ..shemas.ProductSchema import Product
from ..services import ProductService
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get(self, *args, **kwargs):
        products = ProductService.get_all_product()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        phone_object = request.data
        new_product = ProductService.post_product(phone_object)
        serializer = ProductSerializer(data=new_product)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductListDetail(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get(self, id, *args, **kwargs):
        try:
            id = self.kwargs['Id']
            if id is not None:
                print("fuck")
                print(id)
                print("------------")
                product = ProductService.get_product_by_id(id)
                serializer = ProductSerializer(product)
        except:
            return Response({"error": "Cannot find this id"})
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        try:
            id = self.kwargs['Id']
            phone = ProductService.get_product_by_id(id)
            serializer = ProductSerializer(phone, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response('error:Cannot find this product.')

    def delete(self, request, *args, **kwargs):
        id = self.kwargs['Id']
        phone = ProductService.get_product_by_id(id)
        phone.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
