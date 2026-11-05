from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotAllowed
form .forms import PersonForm
# Create your views here.

def hello(request):
    return HttpResponse("Hello World!")

def new(request):
    return HttpResponse("New View!")

def html(request):
    return render(request, 'todos/hello.html')

def index(request,name):
    return HttpResponse(f"Hello {name}!")

def sum(request, a, b):
    return HttpResponse(f"Sum of {a} and {b} is {a+b}")


def persondata(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            return HttpResponse(f"Name: {name}, Age: {age}, Email: {email}")
    else:
       return HttpResponseNotAllowed("POST")

