from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
  print(args,kwargs)
  print(request.user)
  #return HttpResponse("<h1> Hello World</h1> ")
  return render(request,"home.html",{})
# Create your views here.
def contact_view(request,*args, **kwargs):
  return render(request,'contact.html',{})

def about_view(request,*args, **kwargs):
  my_context = {
    "my_text":"this is about me",
    "my_number": 1234,
    "my_list" : ["ABC",187980.23,300000, 1345,2245,167]
  }
  return render(request,"about.html",my_context)

def social_view(request,*args, **kwargs):
  return HttpResponse("<h1>socail page</h1>")