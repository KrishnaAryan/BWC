# Generated by Django 5.0.6 on 2024-07-02 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="projectpage",
            name="client_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="projectpage",
            name="completion",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="projectpage",
            name="manager",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="projectpage",
            name="project_type",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="projectpage",
            name="slug",
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
