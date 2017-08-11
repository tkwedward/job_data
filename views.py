#coding:utf-8#-*-

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.utils import timezone
from .forms import ContactForm, Testform
from .models import Job_detail, Test, User_data_form, Test2, Freelance
from django.contrib.auth.models import User
# 製造頁面

    # 第一頁
def get_name(request):
    form = ContactForm()
    form2 = Testform()
    user = request.user
    return render(request, 'name.html', {'form': form, 'form2':form2, 'type':'normal', 'user':user})


    #第二頁
def job_list(request, types='regular'):#2.1
    # model=None
    if types == 'regular':
        model = Job_detail.objects.order_by('-id')
    elif types == 'freelance':
        model = Freelance.objects.order_by('-id')

    return render(request, 'list_view.html', {'list':model, 'types':types}, )

def job_list_ordering(request, types='regular', order='ascending', by='id'):#2.2
    # try:
    if order == 'ascending':
        order = ''
    elif order == 'descending':
        order = '-'

    rule = order+by

    if types == 'regular':

        model = Job_detail.objects.order_by(rule)

    elif types == 'freelance':
        model = Freelance.objects.order_by(rule)

    return render(request, 'list_view.html', {'list':model, 'types':types})

    # except:
    #     raise Http404('<h1>Page not found</h1>')



def Test_add(request):
    if request.method == "POST":
        form2 = Testform(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect('success')
    else:
        form2 = Testform()
    return render(request, 'name.html', {'form2': form2})

#功能

def added(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if request.user.is_authenticated():
            if form.is_valid():
                data = form.save(commit=False)
                user_id = request.user.id
                post_number = User_data_form.objects.all().filter(user_id=user_id).count()
                if post_number<5:
                    data.save()
                    user = User_data_form.objects.create(user=request.user, data_input= data.pk)
                    return redirect('success')
                else:
                    messages.error(request, 'You have post more than 5 times.')
                    form = ContactForm()
                    return redirect('form')

        else:
            return redirect('social:begin', 'facebook')
            if form.is_valid():
                form.save()
                return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'name.html', {'form': form})

def test_form(request):
    if request.method == "POST":
        number_of_form = int(request.POST.get('number_of_form'))
        date =timezone.now

        for x in range(1, number_of_form+1):
            job_name = request.POST.get('job_name'+str(x))
            job_location = request.POST.get('job_location'+str(x))
            average = request.POST.get('average'+str(x))
            max_salary = request.POST.get('max_salary'+str(x))
            min_salary = request.POST.get('min_salary'+str(x))
            date = timezone.now
            freelance_user_id = request.user

            Freelance.objects.create(job_name=job_name, job_location=job_location, average =average, max_salary= max_salary, min_salary= min_salary, date = '2017-7-3', freelance_user_id=request.user.id)

    return HttpResponse('average= {}, max_salary={}, min_salary={}, request.user= {}'.format(average ,max_salary, min_salary, request.user))


def search(request):
    keyword = request.GET['user_name']
    result = Job_detail.objects.all().filter(company__icontains=keyword)
    return render(request, 'job_search.html', locals())
    # return HttpResponse(keyword)


def example(request):
    return HttpResponse("success<br><a href='/job/form'>back home </a>")
