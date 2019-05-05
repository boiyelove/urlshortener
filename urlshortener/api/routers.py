from rest_framework import routers
from . import viewsets

#router porvide an easy way to automaitcally determine the URL conf.
router = routers.DefaultRouter()
router.register(r'users', viewsets.UserViewSet)
router.register(r'shortlinks', viewsets.ShortLinkViewSet)