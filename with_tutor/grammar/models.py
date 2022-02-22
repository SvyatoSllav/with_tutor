from django.db import models

# Create your models here.

class GrammarMaterial(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
