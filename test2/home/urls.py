from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^logout/$', auth_views.logout, name="logout"),
    url(r'^login/$', auth_views.login,  {'template_name':'memo_app/login.html'}, name="login"),
    url(r'^forus/',views.forus, name="forus")
  
    
]