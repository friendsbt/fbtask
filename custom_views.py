import django
from django.http import HttpResponse

def get_token(request):
    return HttpResponse(django.middleware.csrf.get_token(request))
