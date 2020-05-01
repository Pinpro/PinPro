from django.conf.urls import url, include

from users.views import login_user, logout_user
from pinry.router import drf_router

urlpatterns = [
    url(r'', include(drf_router.urls)),
    url(r'^login/$', login_user, name='login'),
    url(r'^logout/$', logout_user, name='logout'),
]
