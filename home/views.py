from django.shortcuts import render
from hero_section . models import HeroButton,HeroContant,TechnologyUses,TechnologySvg

# Create your views here.
def homeHeroSection(request):
    buttons = HeroButton.objects.all()
    contants = HeroContant.objects.all()
    tech_uses = TechnologyUses.objects.all()
    tech_images = TechnologySvg.objects.all()
    context = {
        "buttons":buttons,
        "contants":contants,
        "tech_uses":tech_uses,
        "tech_images":tech_images,
    }
    return render(request,'home/index.html',context)