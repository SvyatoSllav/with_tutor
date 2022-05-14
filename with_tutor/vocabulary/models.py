from django.db import models

# Create your models here.

class VocabularyMaterial(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    test_link = models.URLField(blank=True, db_index=True)