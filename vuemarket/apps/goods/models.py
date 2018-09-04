from datetime import datetime

from django.db import models

# Create your models here.
from DjangoUeditor.models import UEditorField


class GoodCategory(models.Model):
    """
    商品分类
    """
    CATEGORY_TYPE = (
        (1, '一级类目'),
        (2, '二级类目'),
        (3, '三级类目'),
    )

    name = models.CharField('类别名', default='', max_length=30, help_text='类别名')
    code = models.CharField('类别code', default='', max_length=30, help_text='类别code')
    desc = models.TextField('类别描述', default='', help_text='类别描述')
    category_type = models.CharField('类目级别', choices=CATEGORY_TYPE, help_text='类目级别', max_length=30)
    parent_category = models.ForeignKey('self', models.CASCADE, related_name='sub_cat',
                                        null=True, blank=True, verbose_name='父目录级别',
                                        help_text='父目录'
                                        )
    is_tab = models.BooleanField('是否导航', default=False, help_text='是否导航')
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '商品类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    """
    商品
    """
    category = models.ForeignKey(GoodCategory, on_delete=models.CASCADE, verbose_name='商品类目')
    goods_cn = models.CharField('商品唯一货号', max_length=50, default='')
    name = models.CharField('商品名', max_length=100)
    click_num = models.IntegerField('点击数', default=0)
    sold_num = models.IntegerField('销售量', default=0)
    fav_num = models.IntegerField('收藏数', default=0)
    goods_num = models.IntegerField("库存数", default=0)
    market_price = models.FloatField("市场价格", default=0)
    shop_price = models.FloatField("本店价格", default=0)
    goods_brief = models.TextField("商品简短描述", max_length=500)
    goods_desc = UEditorField(verbose_name='内容', imagePath='goods/images/', width=1000, height=300,
                              filePath='goods/files/', default='')
    ship_free = models.BooleanField('是否承担运费', default=True)
    goods_front_image = models.ImageField('封面图', upload_to='goods/images/', null=True, blank=True)
    is_new = models.BooleanField('是否新品', default=False)
    is_hot = models.BooleanField('是否热销', default=False)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    """
    商品轮播图
    """
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='images', verbose_name='商品')
    image = models.ImageField('图片', upload_to='', null=True, blank=True)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '商品轮播'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    """
    首页轮播商品
    """
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='商品')
    image = models.ImageField('轮播图片', upload_to='banner')
    index = models.IntegerField('轮播顺序', default=0)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '首页轮播'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class HotSearchWords(models.Model):
    """
    搜索栏下方热搜词
    """
    keywords = models.CharField('热搜词', default="", max_length=20)
    index = models.IntegerField('排序', default=0)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '热搜排行'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords
