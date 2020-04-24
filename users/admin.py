from django.contrib import admin
from .models import UserInfo
from django.utils.translation import gettext, gettext_lazy as _

from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
    # 重写fieldsets在admin后台加入自己新增的字段
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('自定义字段'), {'fields': ('birthday', 'gender', 'location', 'mobile', 'blood'
                                 , 'email_verify', 'mobile_verify', 'link')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),

    )


# Django用户继承AbstractUser后密码为明文 造成这个原因是因为在admin注册的生活没有指定Admin
admin.site.register(UserInfo, UserAdmin)
