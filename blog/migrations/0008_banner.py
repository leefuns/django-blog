# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160705_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('banner1', models.ImageField(upload_to=b'banner/%Y-%m-%d', verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe5\x9b\xbe\xe7\x89\x87')),
                ('banner2', models.ImageField(upload_to=b'banner/%Y-%m-%d', verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe5\x9b\xbe\xe7\x89\x87')),
                ('banner3', models.ImageField(upload_to=b'banner/%Y-%m-%d', verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe5\x9b\xbe\xe7\x89\x87')),
                ('banner4', models.ImageField(upload_to=b'banner/%Y-%m-%d', verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe5\x9b\xbe\xe7\x89\x87')),
            ],
            options={
                'verbose_name': '\u5e7f\u544a\u8f6e\u64ad',
            },
        ),
    ]
