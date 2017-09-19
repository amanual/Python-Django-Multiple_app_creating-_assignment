# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
# blosg_app methods:
def index(request):
    response = "Hello, this is first request!"
    return HttpResponse(response)
def new(request):
    request = "Hello, this is from new!"
    return HttpResponse(request)
def create(request):
    request = "Hello, this is from create!"
    return HttpResponse(request)
def show(request, number):
    request = "Hello, this is from show!"
    return HttpResponse(request, number)
def edit(request, number):
    request = "Hello, this is from edit!"
    return HttpResponse(request, number)   
def destroy(request, number):
    request = "Hello, this is from delete!"
    return HttpResponse(request, number)




# Create your views here.
