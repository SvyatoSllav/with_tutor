from django.db import models

# Create your models here.

class ReadingTheme(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        'Image',
        upload_to='reading_theme',
        blank=True
    )


class ReadingSubsections(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        'Image',
        upload_to='Reading_subsections',
        blank=True,

    )
    theme = models.ForeignKey(
        ReadingTheme,
        on_delete=models.CASCADE,
        related_name='reading_subsection',
    )


class ReadingMaterial(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    voice = models.FileField(
        upload_to='reading_voices',
        blank=True)
    image = models.ImageField(
        'Image',
        upload_to='reading_material',
        blank=True
    )
    subsection = models.ForeignKey(
        ReadingSubsections,
        on_delete=models.CASCADE,
        related_name='reading_material',
    )