# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0004_auto_20150209_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='user',
        ),
        migrations.AlterField(
            model_name='folder',
            name='sharing_policy',
            field=models.CharField(default=b'Private', max_length=20, choices=[(b'Private', b'Private'), (b'Public', b'Public'), (b'Protected', b'Protected')]),
            preserve_default=True,
        ),
    ]
