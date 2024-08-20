from django.shortcuts import render
from .models import BannerImage, ReviewImage, SpecialOffer
from .models import CompanyInfo

def mainpage(request):
    banners = BannerImage.objects.all()
    reviews = ReviewImage.objects.all()
    special_offers = SpecialOffer.objects.all()

    context = {
        'banners': banners,
        'reviews': reviews,
        'special_offers': special_offers,
    }
    return render(request, 'home/mainpage.html', context)

def company(request):
    company_info = CompanyInfo.objects.first()
    return render(request, 'home/company_info.html', {'company_info': company_info})