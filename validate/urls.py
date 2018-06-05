'''
Created on Feb 25, 2018

@author: ale_p
'''
from django.conf.urls import url
from validate import views

urlpatterns = [
    url(r'^$', views.index),
    
    ]