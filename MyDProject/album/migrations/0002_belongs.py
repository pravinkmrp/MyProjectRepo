# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Belongs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('folder', models.ForeignKey(to='album.Folder')),
                ('parent', models.ForeignKey(related_name='parent', to='album.Folder')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
