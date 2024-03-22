from django.shortcuts import render
from resume.models import GeneralSetting,ImageSetting

# Create your views here.
def index(request):
    site_title=GeneralSetting.objects.get(name='site_title').parameter
    home_banner=GeneralSetting.objects.get(name='home_banner').parameter
    profile=ImageSetting.objects.get(name='profile').image
    context={
        "site_title":site_title,
        "home_banner":home_banner,
        'profile':profile,
    }
    return render(request,"index.html",context)