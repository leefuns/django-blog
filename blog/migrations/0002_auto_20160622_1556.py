# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '\u4f5c\u8005'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='is_recommend',
        ),
        migrations.AlterField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(to='blog.Author', verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85'),
        ),
    ]
