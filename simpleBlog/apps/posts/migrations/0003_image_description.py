# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='Description',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
