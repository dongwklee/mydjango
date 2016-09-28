# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_inpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inpost',
            old_name='picture',
            new_name='pict',
        ),
    ]
