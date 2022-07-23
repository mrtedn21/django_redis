from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from user_selection.models import User
from user_selection.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
