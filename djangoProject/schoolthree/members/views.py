from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import Member

# Create your views here.

def profile(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        "mymembers": mymembers,
    }
    return HttpResponse(template.render(context, request))
def Details(request, id):
    memberdetails = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        'memberdetails': memberdetails,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apples', 'Oranges', 'Mangoes', 'Cherry']
    }
    return HttpResponse(template.render(context, request))