# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20160919_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='InPost',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('picture', models.ImageField(upload_to='static/')),
            ],
        ),
    ]
