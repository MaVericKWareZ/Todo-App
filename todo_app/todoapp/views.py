from django.http import HttpResponse

# Create your views here.


def index(request) -> HttpResponse:
    return HttpResponse('App is running!')
