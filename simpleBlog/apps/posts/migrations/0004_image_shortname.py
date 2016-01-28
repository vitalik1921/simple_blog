# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_image_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='ShortName',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
