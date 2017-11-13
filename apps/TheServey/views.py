# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def register(request):
    return HttpResponse("<h1> this is the registeation page </h1>")
