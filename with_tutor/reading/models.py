from django.db import models

# Create your models here.
class ReadingMaterial(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()