#coding=utf-8 #coding:utf-8#-*-
from django import forms
from django.forms.widgets import HiddenInput
from .models import Job_detail, User, Freelance, Test
from django.utils.timezone import datetime


OT_choices = (('seldom','絕少'), ('sometimes', '偶爾'), ('often', '經常'), ('always', '幾乎每天'))

OTP_choices=(('yes','有'), ('no','沒有'),  ('not_sure','不知道'))



class Testform(forms.ModelForm):


    class Meta:
        model = Test
        fields = "__all__"

        widgets = {
            'title': forms.TextInput(attrs={'name': 'ck', 'value':'123'}),

            'title2': forms.TextInput(attrs={'name': 'title', 'value':'123'}),

        }

class ContactForm(forms.ModelForm):
    OT = forms.ChoiceField(widget=forms.RadioSelect(), choices=OT_choices)

    Overtime_pay = forms.ChoiceField(widget=forms.RadioSelect(), choices=OTP_choices)


    class Meta:
        model = Job_detail

        labels = {
            "company": "公司名稱",
            "employed": "你現在在職嗎？",
            "position":"職稱",
            "types":"職務型態",
            "place":"工作地點",
            "sex":"性別",
            "salary_type":"薪資類別",
            "salary":"薪資",
            "experience":"年資",
            "working_hour":"一週總工時",
            "OT":"加班頻率",
            "Overtime_pay":"加班費",
            "email":"電郵",
            "date":"日期"
        }

        widgets = {
            'company': forms.TextInput(attrs={'class': 'form-control', 'value':'123'}),

            'position': forms.TextInput(attrs={'class': 'form-control', 'value':'123'}),

            'place': forms.TextInput(attrs={'class': 'form-control', 'value':'123'}),

            'type': forms.Select(attrs={'placeholder': '請選擇', 'value':'full_time'}),

            'salary': forms.TextInput(attrs={'class': 'form-control', 'value':'123'}),

            'sex_choices':forms.Select(attrs={'value':'male'}),

            'working_hour': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '請輸入工時', 'value':'123'}),

            'OT': forms.CheckboxSelectMultiple(attrs={'class': 'form-control', 'value':'seldom'}),

            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email', 'value':'123@gmal.com'})
        }

        error_messages = {
            'company': {
                'required': '請填入資料'
            },
        }

        fields = '__all__'
