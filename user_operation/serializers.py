from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import UserLikes
from core.serializers import PinSerializer


class UserLikesDetailSerializer(serializers.ModelSerializer):
    pin = PinSerializer()

    class Meta:
        model = UserLikes
        fields = ("pin", "id")


class UserLikeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())  # 仅查看当前用户

    class Meta:
        model = UserLikes
        validators = [
            UniqueTogetherValidator(
                queryset=UserLikes.objects.all(),
                fields=('user', 'pin'),
                message="已经点赞"
            )
        ]
        fields = ("user", "pin", "id")
