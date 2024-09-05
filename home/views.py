from django.shortcuts import render
from hero_section . models import HeroButton,HeroContant

# Create your views here.
def home(request):
    button = HeroButton.objects.all()
    contant = HeroContant.objects.all()
    context = {
        "button":button,
        "contant":contant
    }
    return render(request,'home/index.html',context)