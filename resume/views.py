from django.shortcuts import render,redirect
from resume.models import GeneralSetting,ImageSetting,TextSetting,Contact
from django.contrib import messages

# Create your views here.
def index(request):
    site_title=GeneralSetting.objects.get(name='site_title').parameter
    home_banner=GeneralSetting.objects.get(name='home_banner').parameter
    profile=ImageSetting.objects.get(name='profile').image
    text=TextSetting.objects.get(name='description').text

    context={
        "site_title":site_title,
        "home_banner":home_banner,
        'profile':profile,
        'text':text,
    }
    return render(request,"index.html",context)

def contact_message(request):
    if request.method=="POST":
        contact=Contact()
        email=request.POST.get("name")
        text=request.POST.get("text")
        contact.email=email
        contact.text=text
        
