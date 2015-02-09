from django.db import models
from django.conf import settings

# Create your models here.

#class SharingPolicy(models.Model):
#	name = models.CharField(max_length=200)

class Folder(models.Model):
	name=models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	#sharing_policy = models.ForeignKey(SharingPolicy) 
	sharing_policy_list = (
        		('Private', 'Private'),
        		('Public', 'Public'),
			('Protected','Protected'),
	    )
	sharing_policy = models.CharField(max_length=20,choices=sharing_policy_list,
                                      default='Private')

class Belongs(models.Model):
	folder=models.ForeignKey(Folder)
	parent=models.ForeignKey(Folder,related_name='parent')

class File(models.Model):
	folder=models.ForeignKey(Folder)
	name=models.CharField(max_length=200)
	description=models.CharField(max_length=500)
	sharing_policy_list = (
        		('Private', 'Private'),
        		('Public', 'Public'),
			('Protected','Protected'),
	    )
	sharing_policy = models.CharField(max_length=20,choices=sharing_policy_list,
                                      default='Private')
	#user = models.OneToOneField(settings.AUTH_USER_MODEL)
	
