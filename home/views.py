from django.shortcuts import render
from hero_section . models import HeroButton,HeroContant,TechnologyUses,TechnologySvg
from feature.models import Feature,FeatureItem
from about.models import About
from cta.models import *
# Create your views here.
def homeHeroSection(request):
    # for hero section
    buttons = HeroButton.objects.all()
    contants = HeroContant.objects.all()
    tech_uses = TechnologyUses.objects.all()
    tech_images = TechnologySvg.objects.all()

    features= Feature.objects.prefetch_related('featureitem_set').all()
    
    # for about section
    abouts = About.objects.prefetch_related('aboutbutton_set','aboutimage_set','experience_set').all()
    
    # for CTA section 
    ctas = Cta.objects.prefetch_related('ctabutton_set').all()
    context = {
        "buttons":buttons,
        "contants":contants,
        "tech_uses":tech_uses,
        "tech_images":tech_images,
        "features":features,
        "abouts": abouts,
        "ctas": ctas,
    }
    return render(request,'home/index.html',context)