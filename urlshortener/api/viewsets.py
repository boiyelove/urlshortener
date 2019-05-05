from rest_framework import viewsets
from .serializers import UserSerializer, ShortLinkSerializer
from django.contrib.auth import get_user_model
from ..models import ShortLink

User = get_user_model()

#ViewSets define the view behavior
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class ShortLinkViewSet(viewsets.ModelViewSet):
	queryset = ShortLink.objects.all().order_by('-created')
	serializer_class = ShortLinkSerializer