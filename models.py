#coding:utf-8#-*-

from __future__ import unicode_literals

from django.db import models

from django.utils.timezone import datetime
from django.contrib.auth.models import User


# Create your models here.
employed_choices = (('yes','在職'), ('no','無業'))

types_choices=(('full_time','全職'), ('part_time','兼職(含打工)'),  ('interm','實習'), ('temporary','臨時工'), ('contract','約聘雇'),('deliver','派遣'))

sex_choices=(('0', '請選擇'),('male','男'), ('female','女'),  ('other','其他'))

salary_type_choices = (('0', '請選擇'), ('1', '年薪',), ('2', '月薪',), ('3', '日薪',), ('4', '時薪',))

experience_choices=(('0', '請選擇'), ('1','1年或以下'), ('2','2年或以下'), ('3','3年或以下'))

OT_choices = (('seldom','絕少'), ('sometimes', '偶爾'), ('often', '經常'), ('always', '幾乎每天'))

OTP_choices=(('yes','有'), ('no','沒有'),  ('not_sure','不知道'))

CHOICES = (('1', 'First',), ('2', 'Second',))


class Freelance(models.Model):
    job_name = models.CharField( max_length=100)
    job_location = models.CharField( max_length=100)
    average = models.IntegerField(default=None)
    max_salary = models.IntegerField(default=None)
    min_salary = models.IntegerField(default=None)
    date = models.DateField(default=datetime.today())
    freelance_user = models.ForeignKey(User, related_name='freelance_user')

    def __unicode__(self):
        return self.job_name


class Job_detail(models.Model):
    company = models.CharField( max_length=100)

    employed = models.CharField(max_length=100, blank=True, choices= employed_choices, default="no")

    position =  models.CharField( max_length=100, blank=True)

    place =  models.CharField(max_length=100, blank=True)

    types = models.CharField(max_length=100,  choices=types_choices, blank=True, default="full_time")

    sex =  models.CharField(max_length=100,  choices=sex_choices, blank=True, default="male")

    # salary_type = models.CharField(max_length=10,  choices=salary_type_choices, blank='True', default="1")

    salary = models.CharField(max_length=100, blank=True)

    experience =  models.CharField(max_length=100,  choices=experience_choices, blank=True, default="1")

    working_hour = models.DecimalField(blank=True,  decimal_places=2, max_digits=19)

    OT = models.CharField(max_length=100,  choices=OT_choices, blank=False, default="seldom")

    Overtime_pay = models.CharField(max_length=100,  choices=OTP_choices, blank=False, default="no")


    email = models.EmailField(blank=True)

    date = models.DateField(blank=True, default=datetime.today())

    def __unicode__(self):
        return self.company

class User_data_form(models.Model):
    user = models.ForeignKey(User, related_name="user_form")

    def __str__(self):
        return str(self.id)

class Test(models.Model):
    title = models.CharField(max_length=10)
    user = models.ForeignKey(User, related_name="user_test", blank=True, null=True)
    def __str__(self):
        return self.title
