import short_url
from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import ShortLink

@receiver(pre_save, sender=ShortLink)
def shorten_url(sender, instance, **kwargs):
	hex(instance.url)