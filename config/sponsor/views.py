from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from .models import *
from django.views.generic.base import TemplateResponseMixin
from django.views.decorators.http import require_POST




@require_POST
def amount_add(request, Amount_id):
    amount = Amount(request)
    

