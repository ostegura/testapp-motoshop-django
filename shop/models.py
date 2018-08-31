from django.db import models

# Create your models here.
class Menu(models.Model):
	name = models.CharField(max_length = 35, primary_key=True)

	def __str__(self):
		return self.name

class Bikes(models.Model):
	name = models.CharField(max_length = 20)
	year = models.IntegerField()
	price = models.FloatField()
	color = models.CharField(max_length = 20)

	def __str__(self):
		return self.name

class Boots(models.Model):
	name = models.CharField(max_length = 20)
	price = models.FloatField()
	color = models.CharField(max_length = 20)
	size = models.IntegerField()
	description = models.TextField()

	def __str__(self):
		return self.name

class Gloves(models.Model):
	name = models.CharField(max_length = 20)
	price = models.FloatField()
	color = models.CharField(max_length = 20)
	size = models.IntegerField()
	description = models.TextField()

	def __str__(self):
		return self.name

class Combos(models.Model):
	name = models.CharField(max_length = 20)
	price = models.FloatField()
	color = models.CharField(max_length = 20)
	size = models.CharField(max_length = 5)
	description = models.TextField()

	def __str__(self):
		return self.name

class Helmets(models.Model):
	name = models.CharField(max_length = 20)
	price = models.FloatField()
	color = models.CharField(max_length = 20)
	size = models.CharField(max_length = 5)
	description = models.TextField()

	def __str__(self):
		return self.name