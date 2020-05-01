from rest_framework import routers
from core.views import PinViewSet, ImageViewSet, BoardViewSet, TagAutoCompleteViewSet, BoardAutoCompleteViewSet
from user_operation.views import UserLikesViewset
from users.views import UserViewSet, UserListViewSet

drf_router = routers.DefaultRouter()
drf_router.register(r'pins', PinViewSet, basename="pin")
drf_router.register(r'images', ImageViewSet)
drf_router.register(r'boards', BoardViewSet, basename="board")
drf_router.register(r'tags-auto-complete', TagAutoCompleteViewSet)
drf_router.register(r'boards-auto-complete', BoardAutoCompleteViewSet, base_name="board")

drf_router.register(r'like', UserLikesViewset, base_name="user_likes")  # 点赞

drf_router.register(r'users', UserViewSet, base_name="user")
drf_router.register(r'user_list', UserListViewSet, basename="user_list")