from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. 255e54d7 You're at the polls index.")