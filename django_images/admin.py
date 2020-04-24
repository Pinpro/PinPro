from django.contrib import admin

from .models import Image
from .models import Thumbnail


class ImageAdmin(admin.ModelAdmin):

    list_display = ('image_data', 'image', 'height', 'width', )


class ThumbnailAdmin(admin.ModelAdmin):

    list_display = ('original', 'image_data', 'size', 'height', 'width', )


admin.site.register(Image, ImageAdmin)

admin.site.register(Thumbnail, ThumbnailAdmin)
