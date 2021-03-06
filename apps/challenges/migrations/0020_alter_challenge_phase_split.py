# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-07 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("challenges", "0019_added_leaderboard_data_table")]

    operations = [
        migrations.AlterField(
            model_name="challengephasesplit",
            name="visibility",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "host"), (2, "owner and host"), (3, "public")],
                default=3,
            ),
        )
    ]
