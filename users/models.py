import hashlib

from django.db import models
from django.contrib.auth.models import User as BaseUser
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel


class UserInfo(AbstractUser, BaseModel):
    """
        用户表
        """
    GENDER_TYPE = (
        (0, ''),
        (1, '男♂'),
        (2, '女♀'),
        (3, '⚧')
    )

    BLOOD_TYPE = (
        (0, ''),
        (1, 'A'),
        (2, 'B'),
        (3, 'AB'),
        (4, 'O'),
    )

    STATUS_TYPE = (
        ('ONLINE', "在线"),
        ('OFFLINE', "离线")
    )

    VERIFY_STATUS = (
        (0, "未验证"),
        (1, "已验证")
    )

    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.SmallIntegerField(choices=GENDER_TYPE, default="0", verbose_name="性别")
    location = models.CharField(max_length=30, null=True, blank=True, default="", verbose_name="所在城市")
    mobile = models.CharField(max_length=11, null=True, blank=True, default="", verbose_name="电话")
    blood = models.SmallIntegerField(default=0, choices=BLOOD_TYPE, verbose_name='血型')
    email_verify = models.IntegerField(choices=VERIFY_STATUS, default=0, verbose_name="Email是否已经验证")
    mobile_verify = models.IntegerField(choices=VERIFY_STATUS, default=0, verbose_name="Mobile是否已经验证")
    link = models.URLField('个人网址', blank=True, help_text='提示：网址必须填写以http开头的完整形式')

    def gravatar(self):
        return hashlib.md5(self.email.encode('utf-8')).hexdigest()

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
