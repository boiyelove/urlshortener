from rest_framework import routers
from .viewsets import UserViewSet

#router porvide an easy way to automaitcally determine the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)