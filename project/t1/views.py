from django.shortcuts import render_to_response
from project.t1.models import my_info

def index (request):
    info = my_info.objects.get(id = 1)

    return render_to_response('index.html', {'title':'My info', 'info':info})
