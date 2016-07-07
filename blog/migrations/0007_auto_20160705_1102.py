# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160705_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='psot_img',
            field=models.ImageField(upload_to=b'uploads/%Y-%m-%d', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87'),
        ),
    ]
