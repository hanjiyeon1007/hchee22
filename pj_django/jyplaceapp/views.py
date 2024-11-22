from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def mainpg(request):
    template = loader.get_template('mainpg.html')
    return HttpResponse(template.render({},request))
