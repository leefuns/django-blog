# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_banner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': '\u5e7f\u544a\u8f6e\u64ad', 'verbose_name_plural': '\u5e7f\u544a\u8f6e\u64ad'},
        ),
        migrations.RemoveField(
            model_name='banner',
            name='banner1',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='banner2',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='banner3',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='banner4',
        ),
        migrations.AddField(
            model_name='banner',
            name='banner',
            field=models.ImageField(default=b'default.jpg', upload_to=b'banner/%Y-%m-%d', verbose_name=b'\xe8\xbd\xae\xe6\x92\xad\xe5\x9b\xbe\xe7\x89\x87'),
        ),
    ]
