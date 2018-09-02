from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class UserProfile(AbstractUser):
    """
    用户信息
    """
    GENDER_CHOICES = (
        ('male', '男'),
        ('female', '女')
    )

    name = models.CharField('姓名', max_length=30, null=True, blank=True)
    birthday = models.DateTimeField('出生年月', null=True, blank=True)
    gender = models.CharField('性别', max_length=6, choices=GENDER_CHOICES, default='male')
    phone = models.CharField('手机号', max_length=11)
    email = models.EmailField('邮箱', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
