# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160622_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=50, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('email', models.EmailField(max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1')),
                ('message', models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
            ],
            options={
                'verbose_name': '\u8054\u7cfb\u4fe1\u606f',
                'verbose_name_plural': '\u8054\u7cfb\u4fe1\u606f',
            },
        ),
    ]
