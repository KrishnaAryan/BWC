from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.urls import reverse



class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




from django.db import models

class ProjectPage(models.Model):
    CATEGORY_CHOICES = [
        ('interior', 'Interior'),
        ('architecture', 'Architecture'),
        ('building', 'Building'),
        ('exterior', 'Exterior'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    client_name = models.CharField(max_length=100, null=True, blank=True)
    completion = models.CharField(max_length=100, null=True, blank=True)
    project_type = models.CharField(max_length=100, null=True, blank=True)
    manager = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(ProjectPage, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return f"Image for {self.project.title}"





class BlogPost(models.Model):
    image = models.ImageField(upload_to='blog/images/', blank=True, null=True)
    title = models.CharField(max_length=200)
    content_sort = models.CharField(max_length=200)
    content = RichTextField()
    date = models.DateTimeField()
    author = models.CharField(max_length=100)
    click_count = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, max_length=200, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title.replace(" ", "-"))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogpost_detail', args=[self.slug])  # Ensure this matches the URL name



class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_open = models.BooleanField(default=True)  # Add this line
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)  # Add slug field

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title.replace(" ", "-"))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('job_detail', args=[self.slug])




class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True, null=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.job.title}'


class DynamicURL(models.Model):
    path = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=5000, blank=True, null=True)  # Adjusted to a reasonable length
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.path

    def get_absolute_url(self):
        return reverse('dynamic_view', args=[self.path])
    

from django.db import models
from django.utils.text import slugify

class Package(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    package_documents = models.FileField(upload_to='packages')
    color_code = models.CharField(max_length=10,unique=True, blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=200)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Package"
        verbose_name_plural = "Packages"

class PackageSummary(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='package_summaries')
    summary = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.package.name} - {self.summary}"
    
    class Meta:
        verbose_name = "Package Summary"
        verbose_name_plural = "Package Summaries"
