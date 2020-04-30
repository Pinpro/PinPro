from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import UserLikes


# 如果想要让signal信号生效  需要在app.py里面注册一下
@receiver(post_save, sender=UserLikes)
def create_userlike(sender, instance=None, created=False, **kwargs):
    if created:
        pin = instance.pin
        pin.likes_num += 1
        pin.save()


@receiver(post_delete, sender=UserLikes)
def delete_userlike(sender, instance=None, created=False, **kwargs):
    pin = instance.pin
    pin.likes_num -= 1
    pin.save()
