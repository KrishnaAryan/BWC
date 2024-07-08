from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import *

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
            'index', 'about', 'contact',  'blogs', 'job_list', 'PrivacyPolicy', 'TermsConditions', 'service'
        ]

    def location(self, item):
        return reverse(item)

class BlogPostSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.date

class JobDetailSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Job.objects.all()

    def lastmod(self, obj):
        return obj.created_at  # Use the created_at field from the Job model

class DynamicUrlSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return DynamicURL.objects.all()

    def lastmod(self, obj):
        return obj.created_at