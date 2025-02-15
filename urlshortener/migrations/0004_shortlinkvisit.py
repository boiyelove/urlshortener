# Generated by Django 2.2.1 on 2019-05-04 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0003_auto_20190504_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortLinkVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_ip', models.GenericIPAddressField()),
                ('count', models.PositiveIntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('shortlink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='urlshortener.ShortLink')),
            ],
        ),
    ]
