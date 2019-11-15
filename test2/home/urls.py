from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^login/', auth_views.LoginView.as_view(), name="login"),
    url(r'^logout/', auth_views.LogoutView.as_view(), name="logout"),
    url(r'^forus/',views.forus, name="forus")
  
    
]