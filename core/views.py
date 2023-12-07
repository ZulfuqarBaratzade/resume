from django.shortcuts import render
from core.models import GeneralSetting
# Create your views here.


def home(request):
    site_title = GeneralSetting.objects.get(name = 'site_title').parameter
    home_banner_name = GeneralSetting.objects.get(name='home_banner_name').parameter
    home_banner_title = GeneralSetting.objects.get(name='home_banner_title').parameter
    site_description = GeneralSetting.objects.get(name='site_description').parameter

    context = {
        'site_title':site_title,
        'home_banner_name':home_banner_name,
        'home_banner_title':home_banner_title,
        'site_description':site_description,
    }
    return render(request,'index.html',context=context)

