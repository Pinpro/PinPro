from django.contrib import admin

from .models import UserLikes


# Register your models here.
class UserLikesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pin', 'update_time',)
    list_filter = ["user", "pin", ]


admin.site.register(UserLikes, UserLikesAdmin)