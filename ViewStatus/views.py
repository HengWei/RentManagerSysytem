from django.shortcuts import render


# Create your views here.



def ViewStatus(request):
    return render(request, 'ViewStatus.html', locals())
