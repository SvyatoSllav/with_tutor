# Generated by Django 4.0.3 on 2022-05-14 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grammar', '0008_alter_grammarmaterial_voice'),
    ]

    operations = [
        migrations.AddField(
            model_name='grammarmaterial',
            name='test_link',
            field=models.TextField(blank=True),
        ),
    ]