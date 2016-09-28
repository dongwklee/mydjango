# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20160919_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='picture',
            field=models.ImageField(upload_to='static/', default=1),
            preserve_default=False,
        ),
    ]
