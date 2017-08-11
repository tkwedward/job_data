#coding:utf-8#-*-

from django.conf.urls import url
from .views import get_name,  added, example, job_list, job_list_ordering, search, test_form, Test_add


urlpatterns = [
    #第一頁︰用來給人填資料
    url(r'^form$', get_name, name="form"),
    url(r'^form/freelance$', Test_add, name="freelance_form"),

    #第二頁︰用來給人看資料

    url(r'^form/list/(?P<types>[a-z]+)/(?P<order>[a-z]+)/(?P<by>[a-z_]+)/$', job_list_ordering, name="ordering"),

    url(r'^form/list/(?P<types>[a-z]+)/$', job_list, name="latest"),


    # 功能
    url(r'^added$', added, name="added"),
    url(r'^test$', test_form, name="test_form"),
    url(r'^search/*', search, name="search"),
    url(r'^success$', example, name="success"),
]
