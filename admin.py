from django.contrib import admin
from .models import Job_detail, User_data_form, Freelance, Test, Test2
# Register your models here.

admin.site.register(Job_detail)
admin.site.register(Freelance)
admin.site.register(User_data_form)
admin.site.register(Test)
admin.site.register(Test2)
