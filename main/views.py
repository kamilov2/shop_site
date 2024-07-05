from django.shortcuts import render
from .models import Product
from django.views.generic import DetailView


# Create your views here.
def home(request):
    product = Product.objects.all().order_by('-id')
    
    return render(request , 'index.html',{'products':product})


class productDetail(DetailView):
    model = Product
    template_name = 'detail.html'