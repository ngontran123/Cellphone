from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from ..serializers.ProductSerializer import ProductSerializer
from ..shemas.ProductSchema import Product
from ..services import ProductService,UserService
from rest_framework.routers import DefaultRouter
from ..serializers.ProductDetailSerializer import ProductDetailSerializer

router = DefaultRouter()


class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get(self, *args, **kwargs):
        is_products, products = ProductService.get_all_product()
        if not is_products:
            return Response(products)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        role_id = UserService.get_role_by_token(request)
        if role_id != 1:
            raise AuthenticationFailed('You dont have the right to access this feature.')
        phone_object = request.data
        new_product = ProductService.add_product(phone_object)
        serializer = ProductSerializer(data=new_product)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductListDetail(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get(self, request, id, *args, **kwargs):
        is_product, product = ProductService.get_product_by_id(id)
        if not is_product:
            return Response(product)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, *args, **kwargs):
        role_id = UserService.get_role_by_token(request)
        if role_id != 1:
            raise AuthenticationFailed('You dont have the right to access this feature.')
        try:
            object = request.data
            is_product, product = ProductService.get_product_by_id(id)
            if not is_product:
                return Response(product)
            serializer = ProductSerializer(product, data=object)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response('error:Cannot find this product.')

    def delete(self, request, id, *args, **kwargs):
        role_id = UserService.get_role_by_token(request)
        if role_id != 1:
            raise AuthenticationFailed('You dont have the right to access this feature.')
        is_phone, phone = ProductService.get_product_by_id(id)
        if not is_phone:
            return Response(phone)
        phone.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductNameDetail(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get(self, request, pname, *args, **kwargs):
        is_product, product = ProductService.get_product_by_name(pname)
        if not is_product:
            return Response(product)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductBrandDetail(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get(self, request, brand_name, *args, **kwargs):
        is_product, product = ProductService.get_product_by_brand(brand_name)
        if not is_product:
            return Response(product)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductByPriceDetail(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get(self, request, from_price, to_price, *args, **kwargs):
        is_product, products = ProductService.get_product_between_price(from_price, to_price)
        if not is_product:
            return Response(products)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductPaginationDetail(generics.GenericAPIView):
    serializer_class = ProductSerializer

    def get(self, request, page, lim, *args, **kwargs):
        is_product, products = ProductService.pagination(page, lim)
        if not is_product:
            return Response(products)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductAvailable(generics.GenericAPIView):
    serializer_class = ProductSerializer

    def get(self, request, sta, *args, **kwargs):
        is_product, products = ProductService.check_out_of_stock(sta)
        if not is_product:
            return Response(products)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetailView(generics.GenericAPIView):
    serializer_class = ProductDetailSerializer

    def get(self, request, id, *args, **kwargs):
        is_pd, pd = ProductService.get_product_detail_by_id(id)
        if not is_pd:
            return Response(pd)
        serializer = ProductDetailSerializer(pd)
        return Response(serializer.data, status=status.HTTP_200_OK)