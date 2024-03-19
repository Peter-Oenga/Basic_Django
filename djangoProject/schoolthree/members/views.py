from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import Member
from django.db.models import Q

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
    testing_members = Member.objects.all().values()
    table_testing = Member.objects.filter(Q(firstname='Peter') | Q(lastname='Saumu')).values()
    start_with = Member.objects.filter(firstname__startswith='P').values()
    orderBy = Member.objects.all().order_by('-firstname').values()
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Orange', 'Mango', 'Apple', 'Cherry'],
        'start_with': start_with,
        'table_testing': table_testing,
        'greeting': 3,
        'empty_test_object': [],
        'friends': ['Steve', 'DUdu', 'Chris', 'John', 'Makos'],
        'orderBy': orderBy,
        'test_members': testing_members,
        'cars': [
            {
                'brand': 'Ford',
                'model': 'Mustang',
                'year': '1964',
            },
            {
                'brand': 'Ford',
                'model': 'Bronco',
                'year': '1970',
            },
            {
                'brand': 'Volvo',
                'model': 'P1800',
                'year': '1964',
            }
        ]

    }
    return HttpResponse(template.render(context, request))