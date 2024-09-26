from django.shortcuts import render
from hero_section . models import HeroButton,HeroContant,TechnologyUses,TechnologySvg
from feature.models import Feature,FeatureItem
from about.models import About
from cta.models import *
from pricing.models import Pricing,PricingFeature,PricingPlan
from testimonial.models import Testimonial, TestimonialSection
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
    
    # for Pricing 
    pricings = Pricing.objects.all()
    pricing_plans = PricingPlan.objects.prefetch_related('pricingfeature_set').all()
    
    testimonials = Testimonial.objects.all()
    section_content = TestimonialSection.objects.first()
    context = {
        "buttons":buttons,
        "contants":contants,
        "tech_uses":tech_uses,
        "tech_images":tech_images,
        "features":features,
        "abouts": abouts,
        "ctas": ctas,
        "pricings": pricings,
        "pricing_plans":pricing_plans,
        "testimonials":testimonials,
        "section_content":section_content,
        "star_range": range(1, 6),
        
    }
    return render(request,'home/index.html',context)