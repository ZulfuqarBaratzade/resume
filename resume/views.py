from django.shortcuts import render
from resume.models import GeneralSetting

# Create your views here.
def index(request):
    site_title=GeneralSetting.objects.get(name='site_title').parameter
    context={
        "site_title":site_title,
    }
    return render(request,"index.html",context)