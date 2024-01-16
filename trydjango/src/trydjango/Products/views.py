
from django.shortcuts import render
from .forms import ProductForm
from .models import Products






def render_Intial_data(request):
   Intial_data ={
      "title" :"My awesome title"
   }
   form = ProductForm(request.POST or None,initial = Intial_data)
   context={
      "form": form
   }

   return render(request,"products/product_create.html", context)




def product_create_view(request):
    my_form = ProductForm()
    if request.method =="POST":
      my_form = ProductForm(request.POST)
      if my_form.is_valid():
         print(my_form.cleaned_data)
      else:
         print(my_form.errors)
    context = {
       "form":my_form
    }

    return render(request,"products/product_create.html", context)

'''
def product_create_view(request):
    print(request.GET)
    print(request.POST)
    context = {}

    return render(request,"products/product_create.html", context)
'''


def product_create_view(request):
  form = ProductForm(request.POST or None)
  if form.is_valid():
      form.save()

  context = {
    "form": form
    }

  return render(request,"products/product_create.html", context)




def product_detail_view(request):
  obj = Products.objects.get(id=1)
  #context={ 
    #"title" :obj.title,
    #"Discription" : obj.Discription}
  context = {
    "object": obj
    }

  return render(request,"products/product_detail.html", context)


