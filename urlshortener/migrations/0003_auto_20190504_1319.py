# Generated by Django 2.2.1 on 2019-05-04 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('urlshortener', '0002_auto_20190504_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortlink',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shortlink',
            name='author_ip',
            field=models.GenericIPAddressField(default='0.0.0.0'),
            preserve_default=False,
        ),
    ]
