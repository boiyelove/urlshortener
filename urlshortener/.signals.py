from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Link

@receiver(pre_save, sender=Link)
def shorten_url(sender, instance, **kwargs):
	hex(instance.url)