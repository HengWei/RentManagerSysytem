from django.shortcuts import render

# Create your views here.

def TestApp(requesr):
    render(requesr, 'Index.html',locals())