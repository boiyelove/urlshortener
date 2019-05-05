import short_url
from django.db import models
from django.conf import settings

# Create your models here.


# User  =  getattr(Settings, 'AUTH_USER_MODEL')
User =  settings.AUTH_USER_MODEL

class ShortLink(models.Model):
	title = models.CharField(max_length=160, null=True)
	# description = models.TextField(null=True)
	# slug = models.SlugField(unique=True)
	link = models.URLField()
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	author_ip = models.GenericIPAddressField()

	def shortlink(self):
		return short_url.encode_url(self.id)

	@classmethod
	def get_id(cls, shortcode):
		id =  short_url.decode_url(shortcode)
		return cls.objects.get(id = id)

class ShortLinkVisit(models.Model):
	shortlink = models.ForeignKey(ShortLink, on_delete=models.CASCADE)
	visitor_ip = models.GenericIPAddressField()
	count = models.PositiveIntegerField(default=1)
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)