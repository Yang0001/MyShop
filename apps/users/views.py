
from rest_framework import mixins
from rest_framework.mixins import CreateModelMixin

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


User = get_user_model()


class CustomBackend(ModelBackend):
    """
    Custom user authentication
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None




# class UserViewset(CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#     """
#     用户
#     """
#     serializer_class = UserRegSerializer
#     queryset = User.objects.all()
#     authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)