#coding=utf-8 #coding:utf-8#-*-
from django import forms
from django.forms.widgets import HiddenInput
from .models import Job_detail, User, Freelance
from django.utils.timezone import datetime


OT_choices = (('seldom','絕少'), ('sometimes', '偶爾'), ('often', '經常'), ('always', '幾乎每天'))

OTP_choices=(('yes','有'), ('no','沒有'),  ('not_sure','不知道'))

class FreelanceForm(forms.ModelForm):
    job_name = forms.CharField(label='工作名稱', max_length=30)
    job_location = forms.CharField(label='地點', max_length=30)
    date = forms.DateField(label='日期', initial=datetime.today())

    class Meta:
        model = Freelance
        fields = '__all__'

class ContactForm(forms.ModelForm):
    OT = forms.ChoiceField(widget=forms.RadioSelect(), choices=OT_choices)

    Overtime_pay = forms.ChoiceField(widget=forms.RadioSelect(), choices=OTP_choices)


    class Meta:
        model = Job_detail
        widgets = {
            'company': forms.TextInput(attrs={'class': 'form-control', 'value':'123'}),

            'position': forms.TextInput(attrs={'class': 'form-control', 'value':'123'}),

            'place': forms.TextInput(attrs={'class': 'form-control', 'value':'123'}),

            'type': forms.Select(attrs={'placeholder': '請選擇', 'value':'full_time'}),

            'salary': forms.TextInput(attrs={'class': 'form-control', 'value':'123'}),

            'sex_choices':forms.Select(attrs={'value':'male'}),


            'working_hour': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入工時', 'value':'123'}),

            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email', 'value':'123@gmal.com'}),

            'OT': forms.CheckboxSelectMultiple(attrs={'class': 'form-control', 'value':'seldom'}),
# label='Overtime_human_read'
        }

        error_messages = {
            'company': {
                'required': '請填入資料'
            },
        }

        fields = '__all__'
