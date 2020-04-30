from django.apps import AppConfig


# 如果要使用app下面的app.py里面的配置，就要添加Config类到设置文件下面的INSTALLED_APPS里
class UserOperationConfig(AppConfig):
    name = 'user_operation'
    verbose_name = "用户操作管理"

    # signals are imported, so that they are defined and can be used
    def ready(self):
        import user_operation.signals
