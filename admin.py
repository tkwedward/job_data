from django.contrib import admin
from .models import Job_detail, User_data_form, Freelance, Test
# Register your models here.

admin.site.register(Job_detail)
admin.site.register(Freelance)
admin.site.register(User_data_form)
admin.site.register(Test)
