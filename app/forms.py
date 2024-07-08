from django import forms
from .models import *

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    phone = forms.CharField(label='Your Phone', max_length=20)
    message = forms.CharField(label='Your Message', widget=forms.Textarea)





class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'email', 'resume', 'cover_letter']


class DynamicURLData(forms.Form):
	class meta:
		model = DynamicURL
		fields = '__all__'