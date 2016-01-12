# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from .forms import UserForms



def cadastro(request):
    cadastro = UserForms(request.POST or None) 
    if request.method == 'POST':
        if cadastro.is_valid():
            cadastro.save()
        return redirect('/login/')
    return render(request, 'cadastro.html',
                {
                    'cadastro':cadastro,
                }
            )
