# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160707_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='name',
            field=models.CharField(default=b'1', max_length=30, verbose_name=b'\xe8\xbd\xae\xe6\x92\xad\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
    ]
