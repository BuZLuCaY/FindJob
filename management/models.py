from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

import os

def find_picture(instance, fileName):
	url=os.path.splitext(fileName)[-1]
	save_file_name=os.path.join('profile_pictures', str(instance.user.id)+url)
	return save_file_name


class Worker(models.Model):
	tel=models.CharField(max_length=10, blank=True, null=True)
	maritalStatus=models.CharField(max_length=5, blank=True, null=True)
	nationality=models.CharField(max_length=20, blank=True, null=True)
	military=models.CharField(max_length=20, blank=True, null=True)
	drivingLicense=models.CharField(max_length=10, blank=True, null=True)
	university=models.CharField(max_length=30, blank=True, null=True)
	highScholl=models.CharField(max_length=30, blank=True, null=True)
	foreignLanguage=models.CharField(max_length=30, blank=True, null=True)
	dateOfBirth=models.DateField(blank=True, null=True)
	picture=models.ImageField(upload_to='find_picture', blank=True, null=True)
	cv=models.FileField(upload_to='cv', blank=True, null=True)
	address=models.TextField( null=True)
	application=models.TextField(blank=True, null=True)
	projects=models.TextField(blank=True, null=True)
	competencies=models.TextField(blank=True, null=True)
	workExp=models.TextField(blank=True, null=True)
	referance=models.TextField(blank=True, null=True)
	user=models.OneToOneField(User, unique=True)

	def __unicode__(self):
		return u'%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s' % (self.maritalStatus, self.nationality, self.military, self.drivingLicense, self.university,
			self.highScholl, self.foreignLanguage, self.address, self.projects, self.competencies, self.workExp, self.referance)

class Ad(models.Model):
	sector=models.CharField(max_length=30)
	position=models.CharField(max_length=30)
	company=models.CharField(max_length=40)
	tel=models.CharField(max_length=10, blank=True, null=True)
	eMail=models.EmailField(blank=True, null=True)
	date=models.DateField(blank=True, null=True)
	picture=models.ImageField(upload_to='employer', blank=True, null=True)
	address=models.TextField(blank=True, null=True)

	def __unicode__(self):
		return u'%s, %s, %s, %s' % (self.sector, self.position, self.company, self.address)

