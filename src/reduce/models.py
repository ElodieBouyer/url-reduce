from django.db import models

# Create your models here.

class MinUrl(models.Model):
	url_base = models.TextField()
	url_min = models.CharField(max_length=200)
	add_at = models.DateTimeField()
