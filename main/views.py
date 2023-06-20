from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from main.forms import *
from main.models import *


def index(request):
    products = Product.objects.filter(count__gte=1)
    workers = Worker.objects.all()
    if request.method == "POST":
        if request.POST['name'] != '' and request.POST['number'] != '' and request.POST['email'] != '' and request.POST['message'] != '':
            form = Form(name=request.POST['name'], number=request.POST['number'], email=request.POST['email'], message=request.POST['message'])
            form.save()
    return render(request, 'main/index.html', context={'products': products, 'workers': workers})


def services(request):
    if request.method == "POST":
        if request.POST['name'] != '' and request.POST['number'] != '' and request.POST['email'] != '' and request.POST['message'] != '':
            form = Form(name=request.POST['name'], number=request.POST['number'], email=request.POST['email'], message=request.POST['message'])
            form.save()
    return render(request, 'main/services.html')


def repair(request):
    if request.method == "POST":
        if request.POST['name'] != '' and request.POST['number'] != '' and request.POST['email'] != '' and request.POST['message'] != '':
            form = Form(name=request.POST['name'], number=request.POST['number'], email=request.POST['email'], message=request.POST['message'])
            form.save()
    return render(request, 'main/repair.html')


def projects(request):
    projects = Portfolio.objects.all()
    return render(request, 'main/projects.html', context={'projects': projects})


def reviews(request):
    comments = Review.objects.all()
    if request.method == "POST":
        if request.POST['name'] != '' and request.POST['comment'] != '':
            form = Review(name=request.POST['name'], comment=request.POST['comment'])
            form.save()
            return redirect('reviews')
    return render(request, 'main/reviews.html', context={'comments': comments})


def designing(request):
    return render(request, 'main/designing.html')



def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def cards(request, pk):
    product = get_object_or_404(Portfolio, pk=pk)
    return render(request, 'main/cards.html', context={'product': product})


class UserCreations(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy(
        'login'
    )




