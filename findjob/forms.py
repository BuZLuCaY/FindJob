from captcha.fields import CaptchaField
from django.forms import ModelForm
from management.models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import *

class ProfileForm(ModelForm):
	class Meta:
		model = Worker
		fields=('tel','maritalStatus','nationality','military','drivingLicense','university','highScholl',
			'foreignLanguage','dateOfBirth','picture','cv','address','application','projects','competencies','workExp','referance')
	def __init__(self, *args, **kwargs):
  		super(ProfileForm, self).__init__(*args, **kwargs)
		self.fields['tel'].widget.attrs['class'] = 'form-control'
		self.fields['maritalStatus'].widget.attrs['class'] = 'form-control'
		self.fields['nationality'].widget.attrs['class'] = 'form-control'
		self.fields['military'].widget.attrs['class'] = 'form-control'
		self.fields['drivingLicense'].widget.attrs['class'] = 'form-control'
		self.fields['university'].widget.attrs['class'] = 'form-control'
		self.fields['highScholl'].widget.attrs['class'] = 'form-control'
		self.fields['foreignLanguage'].widget.attrs['class'] = 'form-control'
		self.fields['dateOfBirth'].widget.attrs['class'] = 'form-control'


class PostJobForm(ModelForm):
	class Meta:
		model = Ad

class UserRegistrationForm(UserCreationForm):
	captcha=CaptchaField()
	captcha.help_text='Please write character in picture.'
	class Meta:
		model=User
		fields=('first_name','last_name','username','email')

		def clean_email(self):
			if not self.cleaned_data['email']:
				raise forms.ValidationError(u'E-posta adresi girmelisiniz')

			if User.objects.filter(email__iexact=self.cleaned_data['email']):
				raise forms.ValidationError(u"Bu e-posta adresine sahip kullanici mevcut.Baska bir e-posta adresi kullanin.")
			return self.cleaned_data['email']

class AramaFormu(forms.Form):
	aranacak_kelime= forms.CharField(max_length=100, required=True)

	def clean_aranacak_kelime(self):
		kelime=self.cleaned_data['aranacak_kelime']
		if len(kelime)<3:
			raise forms.ValidationError('Search word can not be less than 3 characters')
		return kelime