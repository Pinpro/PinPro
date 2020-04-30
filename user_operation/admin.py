from django.contrib import admin

from .models import UserLikes

# Register your models here.

class UserLikesAdmin(admin.ModelAdmin):
    list_display = ('user', 'pin', 'update_time',)


admin.site.register(UserLikes, UserLikesAdmin)