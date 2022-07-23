from rest_framework import serializers

from user_selection.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            'username',
            'email',
            'groups',
            'role_choice',
            'offer',
            'avatar',
        ]