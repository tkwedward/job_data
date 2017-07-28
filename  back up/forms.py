#coding=utf-8 #coding:utf-8#-*-
from django import forms

employed_choices = (('yes','在職'), ('no','無業'))

types_choices=(('full_time','全職'), ('part_time','兼職(含打工)'),  ('interm','實習'), ('temporary','臨時工'), ('contract','約聘雇'),('deliver','派遣'))

sex_choices=(('male','男'), ('female','女'),  ('other','其他'))

experience_choices=(('1','1年或以下'), ('2','2年或以下'), ('3','3年或以下'))

OT_choices = (('seldom','幾乎不加班'), ('sometimes', '偶爾加班'), ('often', '經常加班'), ('always', '幾乎每天加班'))

OTP_choices=(('yes','有'), ('no','沒有'),  ('not_sure','不知道'))

CHOICES = (('1', 'First',), ('2', 'Second',))




class ContactForm(forms.Form):
    company = forms.CharField(label='Your name', max_length=100)

    employed = forms.ChoiceField(widget=forms.RadioSelect, choices=employed_choices)

    position =  forms.CharField(label='position', max_length=100)

    place =  forms.CharField(label='place', max_length=100)

    types = forms.ChoiceField( choices=types_choices)

    sex =  forms.ChoiceField( choices=sex_choices)

    salary = forms.CharField(label='salary', max_length=100)

    experience =  forms.ChoiceField( choices=experience_choices)

    working_hour = forms.CharField(label='experience', max_length=100)

    OT = forms.ChoiceField(widget=forms.RadioSelect, choices=OT_choices)

    Overtime_pay = forms.ChoiceField(widget=forms.RadioSelect, choices=OTP_choices)

    email = forms.EmailField()


class Contact2Form(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()

    cc_myself = forms.BooleanField(required=False)


    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=types_choices,
    )

    salary = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
