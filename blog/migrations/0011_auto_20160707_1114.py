# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_banner_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='banner',
            new_name='img',
        ),
        migrations.AddField(
            model_name='banner',
            name='index',
            field=models.IntegerField(default=999, verbose_name=b'\xe6\x8e\x92\xe5\x88\x97\xe9\xa1\xba\xe5\xba\x8f(\xe4\xbb\x8e\xe5\xb0\x8f\xe5\x88\xb0\xe5\xa4\xa7)'),
        ),
        migrations.AddField(
            model_name='banner',
            name='url',
            field=models.URLField(null=True, verbose_name=b'\xe5\x9b\x9e\xe8\xb0\x83url', blank=True),
        ),
    ]
