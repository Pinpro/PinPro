from django.contrib import admin

from .models import Pin, Board

# 自定义管理站点的名称和URL标题
admin.site.site_header = 'PinPro Admin'
admin.site.site_title = 'PinPro Admin'


class PinAdmin(admin.ModelAdmin):
    # 注册一下批量处理的方法
    actions = ['make_checked', 'not_passed']  # 请注意这里改成字符串引用了

    # 在amdin里面实现批量操作处理，第一个参数变为self
    def make_checked(self, request, queryset):
        queryset.update(check='1')
    make_checked.short_description = "通过审核"

    def not_passed(self, request, queryset):
        queryset.update(check='2')
    not_passed.short_description = "未通过审核"

    # 遍历tag的queryset 拿出每一个的name值来显示在admin里面
    def tag_name(self, obj):
        return [a.name for a in obj.tags.all()]

    list_display = ('id', 'submitter', 'check', 'private', 'published', 'image_data', 'tag_name', )
    # filter_horizontal = ['likes', ]
    # search_fields = ['check', 'submitter',]
    list_editable = ["check", ]
    list_filter = ["check", "submitter", ]


class BoardAdmin(admin.ModelAdmin):
    # 多对多字段显示在adminlist里面的方法
    def pinsID(self, obj):
        return [a.id for a in obj.pins.all()]

    list_display = ('submitter', 'name', 'private', 'published', 'pinsID')
    filter_horizontal = ['pins', ]


admin.site.register(Pin, PinAdmin)
admin.site.register(Board, BoardAdmin)
