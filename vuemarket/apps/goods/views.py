from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend

from goods.filters import GoodsFilter
from goods.serializers import GoodsSerializer, CategorySerializer
from .models import Goods, GoodCategory
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


# Create your views here.


# class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
#     """
#     商品列表
#     """
#     # def get(self, request, format=None):
#     #     goods = Goods.objects.all()
#     #     goods_serialzer = GoodsSerializer(goods, many=True)
#     #     return Response(goods_serialzer.data)
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

class GoodsPagination(PageNumberPagination):
    """
    商品列表自定义分页
    """
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 10


class GoodsListView(generics.ListAPIView):
    """
    商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination


class GoodsListViewSet(mixins.ListModelMixin):
    """
    商品列表页
    """
    # 定义商品的默认排序
    queryset = Goods.objects.all().order_by('id')
    # 分页
    pagination_class = GoodsPagination
    # 序列化
    serializer_class = GoodsSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)

    filter_class = GoodsFilter
    search_fields = ('=name', 'goods_brief')
    # 排序
    ordering_fields = ('sold_num', 'add_times')


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """
    商品分类列表数据
    """
    queryset = GoodCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer