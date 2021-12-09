from django.db import models
x= [
	('intiated','intiated'),
	('started','started'),
	('outForDelevary','outForDelevary'),
	('deleverd','deleverd')
	]

# Create your models here.
class product(models.Model):
	Pid =  models.IntegerField()
	Pname = models.CharField(max_length=30)
	Pstatus = models.CharField(max_length = 40,choices = x)

	def __str__(self):
		return self.Pname


