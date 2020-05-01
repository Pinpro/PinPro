from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from .models import UserLikes

from core.serializers import PinSerializer
from core.permissions import IsOwnerOrReadOnly, OwnerOnlyIfPrivate
from .serializers import UserLikesDetailSerializer, UserLikeSerializer


# Create your views here.


class UserLikesViewset(viewsets.GenericViewSet, mixins.CreateModelMixin,
                       mixins.ListModelMixin, mixins.DestroyModelMixin,
                       mixins.RetrieveModelMixin):
    """
    list:
        获取用户点赞列表
    retrieve:
        判断某个PIN是否已经点赞
    create:
        点赞
    """
    permission_classes = [IsOwnerOrReadOnly("user"), ]
    lookup_field = "pin_id"

    def get_queryset(self):
        return UserLikes.objects.filter(user=self.request.user)

    # 用get_serializer_class 设置动态的Serializer
    def get_serializer_class(self):
        if self.action == "list":
            return UserLikesDetailSerializer
        elif self.action == "create":
            return UserLikeSerializer
        return UserLikeSerializer
