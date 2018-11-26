# -*- coding: utf-8 -*-
"""
    Created by Huang
    Date: 2018/9/5
"""

from rest_framework import serializers

# class GoodsSerializer(serializers.Serializer):
#     """
#     Serializer实现商品列表页
#     """
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()
from goods.models import Goods, GoodCategory


class CategorySerializer(serializers.ModelSerializer):
    """
    商品类型序列化
    """

    class Meta:
        model = GoodCategory
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):
    """
    商品序列化
    """
    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = '__all__'


class CategorySerializer3(serializers.ModelSerializer):
    """
    三级分类
    """

    class Meta:
        model = GoodCategory
        fields = '__all__'


class CategorySerializer2(serializers.ModelSerializer):
    """
    二级分类
    """
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodCategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """
    商品一级类别序列化
    """
    sub_cat = CategorySerializer2(many=True)  # 'many=True'表示不止一个二级分类

    class Meta:
        model = GoodCategory
        fields = "__all__"
