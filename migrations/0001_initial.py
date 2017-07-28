# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-23 19:45
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Freelance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=100)),
                ('job_location', models.CharField(max_length=100)),
                ('average', models.IntegerField(default=None)),
                ('max_salary', models.IntegerField(default=None)),
                ('min_salary', models.IntegerField(default=None)),
                ('date', models.DateField(default=datetime.datetime(2017, 7, 23, 19, 45, 1, 778010))),
                ('freelance_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='freelance_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('employed', models.CharField(blank=True, choices=[('yes', '\u5728\u8077'), ('no', '\u7121\u696d')], default='no', max_length=100)),
                ('position', models.CharField(blank=True, max_length=100)),
                ('place', models.CharField(blank=True, max_length=100)),
                ('types', models.CharField(blank=True, choices=[('full_time', '\u5168\u8077'), ('part_time', '\u517c\u8077(\u542b\u6253\u5de5)'), ('interm', '\u5be6\u7fd2'), ('temporary', '\u81e8\u6642\u5de5'), ('contract', '\u7d04\u8058\u96c7'), ('deliver', '\u6d3e\u9063')], default='full_time', max_length=100)),
                ('sex', models.CharField(blank=True, choices=[('0', '\u8acb\u9078\u64c7'), ('male', '\u7537'), ('female', '\u5973'), ('other', '\u5176\u4ed6')], default='male', max_length=100)),
                ('salary', models.CharField(blank=True, max_length=100)),
                ('experience', models.CharField(blank=True, choices=[('0', '\u8acb\u9078\u64c7'), ('1', '1\u5e74\u6216\u4ee5\u4e0b'), ('2', '2\u5e74\u6216\u4ee5\u4e0b'), ('3', '3\u5e74\u6216\u4ee5\u4e0b')], default='1', max_length=100)),
                ('working_hour', models.DecimalField(blank=True, decimal_places=2, max_digits=19)),
                ('OT', models.CharField(choices=[('seldom', '\u7d55\u5c11'), ('sometimes', '\u5076\u723e'), ('often', '\u7d93\u5e38'), ('always', '\u5e7e\u4e4e\u6bcf\u5929')], default='seldom', max_length=100)),
                ('Overtime_pay', models.CharField(choices=[('yes', '\u6709'), ('no', '\u6c92\u6709'), ('not_sure', '\u4e0d\u77e5\u9053')], default='no', max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('date', models.DateField(blank=True, default=datetime.datetime(2017, 7, 23, 19, 45, 1, 779504))),
            ],
        ),
        migrations.CreateModel(
            name='User_data_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_count', models.PositiveIntegerField()),
                ('data_input', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_sumbited_by_user', to='job_data.Job_detail')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_form', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
