# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('flatpage_ptr', models.OneToOneField(serialize=False, to='flatpages.FlatPage', auto_created=True, parent_link=True, primary_key=True)),
                ('add_name', models.CharField(max_length=200, blank=True)),
            ],
            bases=('flatpages.flatpage',),
        ),
    ]
