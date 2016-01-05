from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import CadrastroForm


def login(request):
   
    if request.method == 'POST':
        form = CadrastroForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = CadrastroForm()

    return render(request, 'login.html')

