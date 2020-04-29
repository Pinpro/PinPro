from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from .models import UserLikes

from core.permissions import IsOwnerOrReadOnly, OwnerOnlyIfPrivate
from .serializers import UserLikesDetailSerializer, UserLikeSerializer
# Create your views here.


class UserLikesViewset(viewsets.GenericViewSet, mixins.CreateModelMixin,
                     mixins.ListModelMixin, mixins.DestroyModelMixin,
                     mixins.RetrieveModelMixin):
    """
    list:
        获取用户收藏列表
    retrieve:
        判断某个商品是否已经收藏
    create:
        收藏商品
    """
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    permission_classes = [IsOwnerOrReadOnly("user")]

    # 用get_serializer_class 设置动态的Serializer
    # serializer_class = UserFavSerializer
    # authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    lookup_field = "pin_id"

    def get_queryset(self):
        return UserLikes.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return UserLikesDetailSerializer
        elif self.action == "create":
            return UserLikeSerializer
        return UserLikeSerializer

    # 收藏数+1    此处通过信号量signals.py 完成
    # def perform_create(self, serializer):
    #     instance = serializer.save()
    #     goods = instance.goods
    #     goods.fav_num += 1
    #     goods.save()
