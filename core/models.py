import requests

from io import BytesIO

from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.dispatch import receiver

from django_images.models import Image as BaseImage, Thumbnail
from taggit.managers import TaggableManager
# 这个是用来在后台显示缩略图用
from django.utils.html import format_html

from users.models import User


class ImageManager(models.Manager):
    _default_ua = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/48.0.2564.82 Safari/537.36',
    }

    # FIXME: Move this into an asynchronous task
    def create_for_url(self, url, referer=None):
        file_name = url.split("/")[-1].split('#')[0].split('?')[0]
        buf = BytesIO()
        headers = dict(self._default_ua)
        if referer is not None:
            headers["Referer"] = referer
        response = requests.get(url, headers=headers)
        buf.write(response.content)
        obj = InMemoryUploadedFile(buf, 'image', file_name,
                                   None, buf.tell(), None)
        # create the image and its thumbnails in one transaction, removing
        # a chance of getting Database into a inconsistent state when we
        # try to create thumbnails one by one later
        image = self.create(image=obj)
        Thumbnail.objects.get_or_create_at_sizes(image, settings.IMAGE_SIZES.keys())
        return image


class Image(BaseImage):
    objects = ImageManager()

    class Sizes:
        standard = "standard"
        thumbnail = "thumbnail"
        square = "square"

    class Meta:
        proxy = True

    @property
    def standard(self):
        return Thumbnail.objects.get(
            original=self, size=self.Sizes.standard
        )

    @property
    def thumbnail(self):
        return Thumbnail.objects.get(
            original=self, size=self.Sizes.thumbnail
        )

    @property
    def square(self):
        return Thumbnail.objects.get(
            original=self, size=self.Sizes.square
        )



class Board(models.Model):
    class Meta:
        unique_together = ("submitter", "name")
        index_together = ("submitter", "name")

    submitter = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=128, blank=False, null=False)
    private = models.BooleanField(default=False, blank=False)
    pins = models.ManyToManyField("Pin", related_name="pins", blank=True)

    published = models.DateTimeField(auto_now_add=True)

    def image_data(self):
        return format_html(
            '<img src="/static/media/{}" width="100px"/>',
            self.pins.image,
        )

    class Meta:
        ordering = ('-published',)
        verbose_name_plural = '分类'



class Pin(models.Model):
    submitter = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='创建时间')
    private = models.BooleanField(default=False, blank=False)
    url = models.CharField(null=True, blank=True, max_length=256)
    referer = models.CharField(null=True, blank=True, max_length=256)
    description = models.TextField(blank=True, null=True)
    image = models.ForeignKey(Image, on_delete=models.DO_NOTHING, related_name='pin')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='pin_likes')
    published = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    def tag_list(self):
        return self.tags.all()

    def image_data(self):
        # 这里是为了在admin的PIN里面图片显示原始图片 而不是url
        return format_html(
            '<img src="/static/media/{}" width="100px"/>',
            self.image.image,
        )

    def __unicode__(self):
        return '%s - %s' % (self.submitter, self.published)

    def __str__(self):
        # 这里的目的是为了在admin的多对多字段返回图片ID
        return str(self.image.id)

    class Meta:
        ordering = ('-published',)
        verbose_name_plural = 'PIN'


@receiver(models.signals.post_delete, sender=Pin)
def delete_pin_images(sender, instance, **kwargs):
    try:
        instance.image.delete()
    except Image.DoesNotExist:
        pass
