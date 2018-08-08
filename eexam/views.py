from django.shortcuts import render , HttpResponse
from django.views.generic import TemplateView
from .models import Customer
from eexam.forms import TestForm
# Create your views here.

def home(request):
	return render(request, 'login.html')


def base(request):
    return render(request, 'base.html')


#def login(request):
 #   if request.method == 'POST':
  #      print(request.POST)

   # return render(request, 'login.html', {'form': forms.TestForm})

def tform(request):
    if request.method == 'POST':
        if request.POST.get('first_name') and request.POST.get('last_name'):
            post = Customer()
            post.first_name = request.POST.get('first_name')
            post.first_name = request.POST.get('last_name')
            post.save()

            return render(request, 'tform.html')

    else:
        return render(request, 'tform.html')

def insert(request):
    return render(request, 'insert.php')

def inn(request):
    if request.method == 'POST':
        print(request.POST)

    return render(request, 'login.html', {'form': TestForm})