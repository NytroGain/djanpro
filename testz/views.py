from django.shortcuts import render , HttpResponse
from django.views.generic import TemplateView
from .forms import TestForm
# Create your views here.


def inn(request):
    if request.method == 'POST':
        print(request.POST)
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'login.html', {'form': TestForm})