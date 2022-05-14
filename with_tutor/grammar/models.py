from django.db import models

class GrammarTheme(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        'Image',
        upload_to='grammar_theme',
        blank=True
    )


class GrammarSubsections(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        'Image',
        upload_to='grammar_subsections',
        blank=True,

    )
    theme = models.ForeignKey(
        GrammarTheme,
        on_delete=models.CASCADE,
        related_name='grammar_subsection',
    )


class GrammarMaterial(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    test_link = models.URLField(blank=True, db_index=True)
    voice = models.FileField(
        upload_to='grammar_voices',
        blank=True
    )
    image = models.ImageField(
        'Image',
        upload_to='grammar_material',
        blank=True
    )
    subsection = models.ForeignKey(
        GrammarSubsections,
        on_delete=models.CASCADE,
        related_name='grammar_material',
    )
