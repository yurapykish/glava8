# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-27 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_auto_20170126_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ekzamyn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ekzamyn', models.CharField(blank=True, max_length=256, null=True, verbose_name='\u041f\u0440\u0435\u0434\u043c\u0435\u0442')),
                ('ekzamyn_date', models.DateField(blank=True, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0456 \u0447\u0430\u0441 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u043d\u044f')),
                ('teacher', models.CharField(blank=True, max_length=256, null=True, verbose_name='\u0412\u0438\u043a\u043b\u0430\u0434\u0430\u0447')),
            ],
            options={
                'verbose_name': ('\u0435\u043a\u0437\u0430\u043c\u0435\u043d\u0438',),
                'verbose_name_plural': '\u0435\u043a\u0437\u0430\u043c\u0435\u043d\u0438',
            },
        ),
    ]