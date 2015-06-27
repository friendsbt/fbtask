import json
import django
from django.http import HttpResponse

def get_token(request):
    token = django.middleware.csrf.get_token(request)
    data = '%s("%s");' % (request.REQUEST['callback'], token)
    return HttpResponse(data, "text/javascript")
