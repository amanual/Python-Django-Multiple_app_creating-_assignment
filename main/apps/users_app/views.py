# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from models import *
# Create your views here.
def users(request):
    request = "Hello, this is from Users!"
    return HttpResponse(request)
def register(request):
    request = "Hello, this is from register!"
    return HttpResponse(request)
def users_new(request):
    request = "Hello, this is from users_new!"
    return HttpResponse(request)
def login(request):
    request = "Hello, this is from login!"
    return HttpResponse(request)

# Create your views here.
