# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from models import *
# Create your views here.
def surveys(request):
    request = "Hello, this is from Survers!"
    return HttpResponse(request)
def new(request):
    request = "Hello, this is from Survers New!"
    return HttpResponse(request)