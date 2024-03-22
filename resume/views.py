from django.shortcuts import render
from resume.models import GeneralSetting

# Create your views here.
def index(request):
    site_title=GeneralSetting.objects.get(name='site_title').parameter
    home_banner=GeneralSetting.objects.get(name='home_banner').parameter
    context={
        "site_title":site_title,
        "home_banner":home_banner,
    }
    return render(request,"index.html",context)