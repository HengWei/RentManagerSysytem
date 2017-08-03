from django.shortcuts import render
from MainDashboard.models import Info


# Create your views here.

def TestApp(request):
    # request.session['managerId'] = 1
    data = Info.object.GetRoomOverView()
    return render(request, 'Index.html', locals())
