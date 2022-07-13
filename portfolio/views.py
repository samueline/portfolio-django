from django.http import HttpResponse
from django.shortcuts import render

from portfolio.forms import NameForm
from .models import Contact, Project

def home(request):
    projects =Project.objects.all()
    return render(request, 'home.html',{'projects':projects})


def post(request):
    # print(request.POST)
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['user']
            em = form.cleaned_data['email']
            de = form.cleaned_data['descripcion']
            reg = Contact(user=nm, email=em, descripcion=de)
            reg.save()
            # return HttpResponse('Yay valid')
    else:
        form = NameForm()
    context = {}
    return render(request, 'home.html', {'form': form})