from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import generics, status
from ..serializers.ProductDetailSerializer import ProductDetailSerializer
from ..services import ProductDetailService,UserService
from rest_framework.routers import DefaultRouter


class ProductDetailListView(generics.ListAPIView):
    serializer_class = ProductDetailSerializer

    def get(self, request, *args, **kwargs):
        is_pd, pd = ProductDetailService.get_product_detail()
        if not is_pd:
            return Response(pd)
        serializer = ProductDetailSerializer(pd, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        role_id = UserService.get_role_by_token(request)
        if role_id != 1:
            raise AuthenticationFailed('You dont have the right to access this feature.')
        object = request.data
        serializer = ProductDetailSerializer(data=object)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetailApiView(generics.GenericAPIView):
    serializer_class = ProductDetailSerializer

    def get(self, request, id, *args, **kwargs):
        is_pd, pd = ProductDetailService.get_product_detail_by_id(id)
        if not is_pd:
            return Response(pd)
        serializer = ProductDetailSerializer(pd)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, *args, **kwargs):
        role_id = UserService.get_role_by_token(request)
        if role_id != 1:
            raise AuthenticationFailed('You dont have the right to access this feature.')
        is_pd, pd = ProductDetailService.get_product_detail_by_id(id)
        object = request.data
        if not is_pd:
            return Response(pd)
        serializer = ProductDetailSerializer(pd, data=object)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id, *args, **kwargs):
        role_id = UserService.get_role_by_token(request)
        if role_id != 1:
            raise AuthenticationFailed('You dont have the right to access this feature.')
        is_pd, pd = ProductDetailService.get_product_detail_by_id(id)
        if not is_pd:
            return Response(pd)
        pd.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)