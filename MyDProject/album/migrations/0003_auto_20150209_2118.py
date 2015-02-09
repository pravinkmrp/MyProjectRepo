# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('album', '0002_belongs'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='user',
            field=models.OneToOneField(default=None, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='sharing_policy',
            field=models.CharField(default=b'Private', max_length=20, choices=[(b'Private', b'Private'), (b'Public', b'Public'), (b'Protected', b'Protected')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='folder',
            name='sharing_policy',
            field=models.CharField(default=b'Private', max_length=20, choices=[(b'Private', b'Private'), (b'Public', b'Public'), (b'Protected', b'Protected')]),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='SharingPolicy',
        ),
    ]
