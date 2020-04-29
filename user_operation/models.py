from django.db import models
from core.models import Pin
from users.models import UserInfo
from db.base_model import BaseModel


class UserLikes(BaseModel):
    """
    Pin
    """
    user = models.ForeignKey(UserInfo, verbose_name="用户")
    pin = models.ForeignKey(Pin, verbose_name="Pin", help_text="Pin图")

    class Meta:
        verbose_name = "用户点赞"
        verbose_name_plural = verbose_name
        unique_together = ("user", "pin")

    def __str__(self):
        return self.user.username
