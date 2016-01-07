from django.shortcuts import render

from .forms import UsuarioForm


def login(request):
    form = UsuarioForm()
    
        
    return render(request, 'login.html',
                    {'form':form}
                 )
