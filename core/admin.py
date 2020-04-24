from django.contrib import admin

from .models import Pin, Board

# 自定义管理站点的名称和URL标题
admin.site.site_header = '网站管理'
admin.site.site_title = '2zzy后台管理'


class PinAdmin(admin.ModelAdmin):

    list_display = ('id', 'submitter', 'private', 'published', 'image_data', 'tag_list', )
    filter_horizontal = ['likes', ]

class BoardAdmin(admin.ModelAdmin):
    # 多对多字段显示在adminlist里面的方法
    def pinsID(self, obj):
        return [a.id for a in obj.pins.all()]

    list_display = ('submitter', 'name', 'private', 'published','pinsID')
    filter_horizontal = ['pins', ]


admin.site.register(Pin, PinAdmin)
admin.site.register(Board, BoardAdmin)
