from django.db import models
from django.contrib.auth.models import User
# import uuid

# Create your models here.

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	first_name = models.CharField(max_length=150,blank=True)
	last_name = models.CharField(max_length=150,blank=True)
	email = models.EmailField(max_length=100)
	birth_date = models.DateField(blank=True)
	# userid = models.IntegerField()

	def __str__(self):
		return self.user.username