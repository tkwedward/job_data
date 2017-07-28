#coding:utf-8#-*-

from django.conf.urls import url
from .views import get_name, get_name_2, added, example, job_list, job_list_work_time, job_list_salary, search, customer_order,  Freelance_add


urlpatterns = [
    #第一頁︰用來給人填資料
    url(r'^form$', get_name, name="form"),
    url(r'^form/freelance$', get_name_2, name="freelance_form"),

    #第二頁︰用來給人看資料

    url(r'^form/working_hour$', job_list_work_time, name="working_hour"),
    url(r'^form/salary$', job_list_salary, name="salary"),
    url(r'^form/latest$', job_list, name="latest"),


    # 功能
    url(r'^added$', added, name="added"),
    url(r'^freelance_added$', Freelance_add, name="freelance_added"),
    url(r'^search/*', search, name="search"),
    url(r'^order/*', customer_order, name="order"),
    url(r'^success$', example, name="success"),
]
