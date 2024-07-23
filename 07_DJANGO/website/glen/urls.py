from django.urls import path, re_path
from glen.views import GlenTemplateView, SuperListView, SubListView, SuperDetailView, SubDetailView
from django.views.generic import TemplateView
from . import views





app_name = 'glen'
urlpatterns = [
    re_path(r'^$', views.greetglen, name='greetglen'),                     # /glen/
    re_path(r'^greet$', views.greet, name='greet'),
    #re_path(r'^2g$', views.greetglen, name='greetglen2'),                 # /glen/2g/
    re_path(r'^today$', views.today, name='today'),                        # /glen/today/
    re_path(r'^getform$', views.get_form, name='getform'),                 # /glen/getform/
    re_path(r'^getresult$', views.get_result, name='getresult'),
    re_path(r'^postform$', views.post_form, name='postform'),
    re_path(r'^postresult$', views.post_result, name='postresult'),
    re_path(r'^redirect$', views.redirect_view, name='redirect'),
    re_path(r'^extension$', views.extension, name='extension'),
    re_path(r'^positional/(\d{2})/(\d{4})/$', views.positional_args, name='positional'),          # /glen/positional/02/1995/
    re_path(r'^keyword/(?P<month>\d{2})/(?P<year>\d{4})/$', views.keyword_args, name='keyword'),  # /glen/keyword/02/1995/
    re_path(r'^sendemail/$', views.send_email, name='send_email'),                                # /glen/send_email/
    re_path(r'^static1/$', GlenTemplateView.as_view()),                                           # /glen/static1/     -- uses django Generic Views defined in views.py
    re_path(r'^static2/$', TemplateView.as_view(template_name='glen\static2.html')),              # /glen/static2/     -- doesn't even need a class in views.py
    re_path(r'^listview/$', SuperListView.as_view()),                                             # /glen/listview/        -- uses Generic Views
    re_path(r'^sublistview/$', SubListView.as_view()),                                            # /glen/sublistview/        -- uses Generic Views
    re_path(r'^detailview/(?P<pk>\d+)/$', SuperDetailView.as_view()),                             # /glen/detail/      -- uses Generic DetailView, requires ?P<pk>
    re_path(r'^subdetailview/(?P<pk>\d+)/$', SubDetailView.as_view()),                            # /glen/subdetail/      -- uses Generic DetailView, requires ?P<pk>
    re_path(r'^login/', TemplateView.as_view(template_name='glen\login.html')),                   # /glen/connect/
    re_path(r'^loggedin/', views.loggedin, name='loggedin'),                                      # /glen/login/
    re_path(r'^session/', views.session_data, name='session_data'),                               # /glen/sessiondata/
    ]
