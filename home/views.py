from django.shortcuts import render
from hero_section . models import HeroButton,HeroContant,TechnologyUses,TechnologySvg
from feature.models import Feature,FeatureItem
# Create your views here.
def homeHeroSection(request):
    # for hero section
    buttons = HeroButton.objects.all()
    contants = HeroContant.objects.all()
    tech_uses = TechnologyUses.objects.all()
    tech_images = TechnologySvg.objects.all()

    features= Feature.objects.prefetch_related('featureitem_set').all()

    context = {
        "buttons":buttons,
        "contants":contants,
        "tech_uses":tech_uses,
        "tech_images":tech_images,
        "features":features,
    }
    return render(request,'home/index.html',context)