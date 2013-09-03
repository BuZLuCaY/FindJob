# Create your views here.
from django.shortcuts import render, render_to_response, redirect
from findjob.forms import *
from django.db.models import Q
from django.http import HttpResponse
from management.models import *
from django.contrib.auth import *
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.db.models.signals import post_save

def index(request):
	ads=Ad.objects.all().order_by('-date')
	return render(request, 'index.html', {"ads": ads,})

def postJob(request):
	form = PostJobForm()
	if request.method == 'POST':
		form = PostJobForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('mainPage')
	else:
		form = PostJobForm()
	return render(request, 'postJob.html', {"form": form,}) 

def profile(request):
	if request.user.is_authenticated():
		my_profile = Worker.objects.get(user=request.user)
		my_user = request.user

		if request.method == 'POST':
			form = ProfileForm(request.POST, request.FILES, instance=my_profile)
			if form.is_valid():
				form.save()
				return redirect('mainPage')
		else:
			form = ProfileForm(instance=my_profile)

		return render(request, 'profile.html', {"form": form, "my_profile":my_profile, "my_user":my_user})
	else:
		return redirect('register')

def profile_pictures(request, picture_name):
	file_url=os.path.join(settings.MEDIA_ROOT, 'profile_pictures', picture_name)
	if os.path.exists(file_url):
		picture=os.path.join(settings.MEDIA_ROOT, 'profile_pictures', picture_name)
		url=os.path.splitext(picture_name)[-1][1:]
		mime_type=mimetype='image/%s' % url
		picture_data=open(picture, "rb").read()
		return HttpResponse(picture_data, mimetype=mime_tipi)
	else:
		picture_data=open(os.path.join(settings.MEDIA_ROOT, 'not.png'), "rb").read()
		return HttpResponse(picture_data, mimetype='image/png')

def register(request):
	if request.method == 'POST':
		form=UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			kullanici=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
			if kullanici.is_authenticated():
				login(request, kullanici)
			return redirect('mainPage')
	else:
		form=UserRegistrationForm()
	return render_to_response('registration/register.html', locals(), context_instance=RequestContext(request))

def contact(request):
	return render(request,'contact.html')

def google(request):
	return render(request,'google.html')

def createWorker(sender, instance, created, **kwargs):
	if created:
		Worker.objects.create(user=instance)

post_save.connect(createWorker, sender=User)

def search(request):
	arama_formu=AramaFormu()
	if request.GET.get('aranacak_kelime'):
		arama_formu=AramaFormu(request.GET)
		if arama_formu.is_valid():
			aranacak_kelime=arama_formu.cleaned_data['aranacak_kelime']
			ads=Ad.objects.filter(Q(company__contains=aranacak_kelime) | Q(sector__contains=aranacak_kelime) | Q(position__contains=aranacak_kelime))
			print ads
	return render_to_response('search.html', locals(), context_instance=RequestContext(request))