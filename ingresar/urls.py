'''
Created on Feb 25, 2018

@author: ale_p
'''
from django.conf.urls import url

from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', login, {'template_name': 'ingresar/login.html'}),
    ]