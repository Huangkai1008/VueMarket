from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from goods.models import Goods

User = get_user_model()


class UserFav(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='商品', help_text='商品id')
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        unique_together = ('user', 'goods')

    def __str__(self):
        return self.user.username


class UserAddress(models.Model):
    """
    用户收货地址
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    province = models.CharField('省份', max_length=100, default='')
    city = models.CharField('城市', max_length=100, default='')
    district = models.CharField('区域', max_length=100, default='')
    address = models.CharField('详细地址', max_length=100, default='')
    signer_name = models.CharField('签收人', max_length=100, default='')
    signer_mobile = models.CharField('电话', max_length=11, default='')
    add_time = models.DateTimeField('添加时间', default=datetime.now)