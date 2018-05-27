from django.conf.urls import url

from . import views

app_name = 'subs'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^r/(?P<sub_name>[a-zA_Z]+)/$', views.view_sub, name='view_sub'),

]