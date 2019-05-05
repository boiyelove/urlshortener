from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import ShortLink

User = get_user_model()

#Serializers define the API representation
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'is_staff')

class ShortLinkSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ShortLink
		fields = ('url', 'title', 'link', 'shortlink', 'created', 'updated')