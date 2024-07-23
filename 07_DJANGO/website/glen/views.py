
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import User, auth  # used for user authentication
from django.contrib import messages # these are like flash messages in Flask   messages.info() messages.warning() e.t.c
from django.views.generic import TemplateView, ListView, DetailView
from .forms import LoginForm
from .models import Super,Sub
from datetime import datetime as dt


# Create your views here.
def greetglen(request):
    return HttpResponse('<h1>Hi Glen!</h1>')

def greet(request):
    return render(request,'greetings.html')

def today(request):
    context = {}
    context['today'] = dt.now()
    context['weekdays'] = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']  # can pass list objects to the context
    context['names'] = {'First':'fred', 'Second': 'Tom'}
    return render(request,r'glen\today.html', context)

def extension(request):
    context = {}
    context['mytitle'] = 'this title was injected'
    context['mycontent'] = 'this body was injected'
    return render(request,r'glen\extension.html', context)

def get_form(request):
    context = {}
    return render(request,r'glen\mygetform.html', context)

def get_result(request):
    html =f"request.GET['gettext']={request.GET['gettext']}"
    return HttpResponse(html)

def post_form(request):
    context = {}
    return render(request,r'glen\mypostform.html', context)

def post_result(request):
    bl = bool(request.POST)
    html =f"{bl}<br>request.POST['posttext']={request.POST['posttext']}"
    return HttpResponse(html)

def redirect_view(request):
    return redirect('http://google.com')  # can use an internal url path name too e.g. redirect('today')

def positional_args(request, param1, param2):  # takes parameters in order from the URL
    html = f'you entered {param1}, {param2}'
    return HttpResponse(html)

def keyword_args(request, year, month):       # note order of year,month doesn't matter
    html = f'you entered {month}, {year}'
    return HttpResponse(html)

# example of a django generic view of wich there are 10 in django
# ['ArchiveIndexView', 'CreateView', 'DateDetailView', 'DayArchiveView','DeleteView', 'DetailView', 'FormView',
# 'GenericViewError', 'ListView','MonthArchiveView', 'RedirectView', 'TemplateView', 'TodayArchiveView','UpdateView',
# 'View', 'WeekArchiveView', 'YearArchiveView']

class GlenTemplateView(TemplateView):  # used for a static template
   template_name = "glen\static.html"  # looks in the glen\template directory

class SuperListView(ListView):
    model = Super
    #template_name = "glen\my_list.html"  # This would override the default list_view template which is glen\super_list.html
    #context_object_name = 'all_supers'   # This would override the default which is 'object_list' collection in templates
    # def get_queryset(self):
    #     return Super.objects.all()

class SubListView(ListView):
    model = Sub
    #queryset = Sub.objects.all()[:4]  # This would override the default queryset = Sub.objects.all()
    # def get_queryset(self):          # I think this is another way to override default queryset
    #     return Sub.objects.all()[:4]


class SuperDetailView(DetailView):
    model = Super
    template_name = 'glen\detail.html'        # default is 'glen\super_detail.html'
    def get_queryset(self):
        return Super.objects.all()

class SubDetailView(DetailView):
    model = Sub
    template_name = 'glen\sub_detail.html'        # these are defaults,  I didn't need to write this line
    queryset = Sub.objects.all()                  # these are defaults,  I didn't need to write this line


class StaticView(TemplateView):
   template_name = "static.html"


def send_email(request):
    subject = 'Test Email from django!!!'
    html_message = 'hope this<br>works'
    from_email = 'itreports@tscinsurance.com'  # can not set to any other value
    mail_to = ['bezoren@gmail.com']
    res = send_mail(subject=subject, message='', from_email=from_email, recipient_list=mail_to, html_message=html_message)  # 0 = Failure, 1 = Success
    html = f'Result={res}<br>Your message has been sent!'
    return HttpResponse(html)

    # send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)
    # subject − E-mail subject.
    # message − TEXT E-mail body - this needs to be present even if overridden by html_message
    # from_email − E-mail from.
    # recipient_list − List of receivers’ e-mail address.
    # fail_silently − Bool, if false send_mail will raise an exception in case of error.
    # auth_user − User login if not set in settings.py.
    # auth_password − User password if not set in settings.py.
    # connection − E-mail backend.
    # html_message − (new in Django 1.7) if present, the e-mail will be multipart/alternative, if using set message='' as a parameter

    # see https://www.tutorialspoint.com/django/django_sending_emails.htm  for
    # send_mass_mail  - sends multiple emails
    # mail_managers  - sends email to people in django ADMIN

def loggedin(request):
    context = {}

    username = "not logged in"
    password = "not logged in"

    if request.method == "POST":
        # Get the posted form
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
            password = MyLoginForm.cleaned_data['password']
    else:
        MyLoginForm = LoginForm()  # not sure what this is doing ????

    context['username'] = username
    context['password'] = password


    # context['username'] = request.POST['username']  -- this is the old way to do it
    # context['password'] = request.POST['password']  -- this is the old way to do it
    return render(request, 'glen\loggedin.html', context)


def session_data(request):
    # request.session is treated as a dictionary
    # request.session['value'] =   .. will set
    # del request.session['value'] .. will delete e.t.c.
    # by default session data stored in the database not in cookies (more secure

    num_supers = Super.objects.count()  # The 'all()' is implied by default.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    # request.session.modified = True  # not sure when this is requried
    html = f'Total Supers:{num_supers}, Total Visits:{num_visits}'
    return HttpResponse(html)