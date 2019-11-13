# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('contont', models.TextField()),
                ('priority_level', models.SmallIntegerField()),
                ('status', models.SmallIntegerField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('expire_time', models.DateField(null=True, blank=True)),
                ('last_modify_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
