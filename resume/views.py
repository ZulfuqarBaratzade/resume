from django.shortcuts import render,redirect,HttpResponseRedirect
from resume.models import GeneralSetting,ImageSetting,TextSetting,Contact
from django.contrib import messages
from resume.forms import ContactForm
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
    url=request.META.get("HTTP_REFERER")
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            message=form.save(commit=False)
            message.save()
            
            return redirect("index")
        else:
            context['form'] = ContactForm()
        messages.success(request,"Thanks")
    return render(request,"index.html",context)

# def contact_message(request):
#     context=dict()
#     url=request.META.get("HTTP_REFERER")
#     if request.method=="POST":
#         form=ContactForm(request.POST)
#         if form.is_valid():
#             message=form.save(commit=False)
#             message.save()
#             return HttpResponseRedirect(url)
#         else:
#             context['form'] = ContactForm()
        

        
