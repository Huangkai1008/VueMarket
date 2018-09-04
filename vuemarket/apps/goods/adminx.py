# -*- coding: utf-8 -*-
"""
    Created by Huang
    Date: 2018/9/4
"""
import xadmin
from goods.models import GoodsImage, Goods, GoodCategory


class GoodAdmin(object):
    """
    商品
    """
    # 显示的列
    list_display = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                    "shop_price", "goods_brief", "goods_desc", "is_new", "is_hot", "add_time"]
    # 可以搜索的字段
    search_fields = ['name']
    # 列表页可以直接编辑的
    list_editable = ["is_hot"]
    # 过滤器
    list_filter = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                   "shop_price", "is_new", "is_hot", "add_time", "category__name"]
    # 富文本编辑器
    style_fields = {"goods_desc": 'ueditor'}

    # 添加商品的时候可以添加商品图片
    class GoodsImageInline(object):
        model = GoodsImage
        exclude = ['add_time']
        extra = 1
        style = 'tab'

    inlines = [GoodsImageInline]


class GoodsCategoryAdmin(object):
    """
    商品分类
    """
    list_display = ['name', 'category_type', 'parent_category', 'add_time']
    list_filter = ['category_type', 'parent_category', 'name']
    search_fields = ['name']


xadmin.site.register(Goods, GoodAdmin)
xadmin.site.register(GoodCategory, GoodsCategoryAdmin)


