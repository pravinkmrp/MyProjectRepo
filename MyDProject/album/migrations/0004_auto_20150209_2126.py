# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_auto_20150209_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='sharing_policy',
            field=models.CharField(default=b'Private', max_length=20, choices=[(b'Private', b'Private'), (b'Public', b'Public'), (b'Protected', b'Protected'), (b'Unknown', b'Unknown')]),
            preserve_default=True,
        ),
    ]
