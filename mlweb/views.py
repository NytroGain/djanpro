from django.shortcuts import render
from eexam.forms import TestForm
from testz.forms import TestForm

def home(request):
    return render(request, 'home.html')
def index(request):
    return render(request, 'index.html')
def form(request):
    return render(request, 'form.php')

def index2(request):
    return render(request, 'index2.html')
def index3(request):
    return render(request, 'index3.html')
def predicpage (request):
    return render (request, 'predicpage.html')
def abc (request):
    return render (request, 'abc.html')
def connect (request):
    return render (request, 'connect.php')

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

def emailtest(request):
    if request.method == 'POST':
        print(request.POST)

    return render(request, 'eexam/login.html', {'form': TestForm})

def inn(request):
    if request.method == 'POST':
        print(request.POST)

    return render(request, 'testz/login.html', {'form': TestForm})
#def exampage (request):
    # get all published exams
   ##exams = Exam.objects.filter(published=True)
    # get exam by id
   ## id = request.GET.get('id')
   ## if id:
      ## exam = Exam.objects.get(pk=id)
   ## return render(request, 'exampage.html', {'exams': exams, 'exam': exam})