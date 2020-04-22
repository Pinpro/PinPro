from django.contrib import admin

from .models import Pin, Board

# 自定义管理站点的名称和URL标题
admin.site.site_header = '网站管理'
admin.site.site_title = '2zzy后台管理'

class PinAdmin(admin.ModelAdmin):
    list_display = ('submitter', 'private','published','image_data','tag_list')


admin.site.register(Pin, PinAdmin)
admin.site.register(Board)
