# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20160919_1736'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InPost',
        ),
    ]
