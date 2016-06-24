# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160622_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='authors',
        ),
        migrations.AddField(
            model_name='article',
            name='authors',
            field=models.CharField(default=b'admin', max_length=100, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85'),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
