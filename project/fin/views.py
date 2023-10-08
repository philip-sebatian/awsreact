from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request,'index.html')