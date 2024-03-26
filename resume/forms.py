from django.forms import ModelForm
from resume.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields=['email','text']
