# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20160922_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='none_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
