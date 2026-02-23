from django.http import HttpResponse

def home(request):
     return HttpResponse("Hello World!!")

def about(request):
     return HttpResponse("About us")

def contact(request):
     return HttpResponse("Contact us")
