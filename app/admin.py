from django.contrib import admin
from .models import *

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message', 'timestamp']
    search_fields = ['name', 'email', 'phone', 'timestamp']
    list_filter = ['timestamp']






# Register your models here.

from django.contrib import admin
from .models import ProjectPage, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(ProjectPage)
class ProjectPageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category','client_name','completion','project_type','manager','slug']  # Adjusted list_display
    list_filter = ['category']  # Adjusted list_filter
    search_fields = ['title', 'description']
    inlines = [ProjectImageInline]

@admin.register(ProjectImage)
class ProjectPageImageAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return obj.image.url if obj.image else None
    image_tag.short_description = 'Image'  # Custom image_tag method
    list_display = ['project', 'image_tag']
    readonly_fields = ['image_tag']
    search_fields = ['project__title']







admin.site.register(BlogPost)


from django.contrib import admin
from django.utils.html import format_html
from .models import Job, Application

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_open')
    list_filter = ('is_open', 'created_at')
    search_fields = ('title', 'description')
    actions = ['make_open', 'make_closed']

    @admin.action(description='Mark selected jobs as open')
    def make_open(self, request, queryset):
        queryset.update(is_open=True)

    @admin.action(description='Mark selected jobs as closed')
    def make_closed(self, request, queryset):
        queryset.update(is_open=False)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'job', 'applied_at', 'download_resume')
    list_filter = ('job', 'applied_at')
    search_fields = ('name', 'email', 'job__title')

    def download_resume(self, obj):
        if obj.resume:
            return format_html('<a href="{}" download>Download</a>', obj.resume.url)
        return "No resume uploaded"
    download_resume.short_description = 'Resume'







# @admin.register(DynamicURL)
# class DynamicURLAdmin(admin.ModelAdmin):
#     list_display = ('path', 'title')
#     search_fields = ('path', 'title')


from import_export.admin import ImportExportModelAdmin
@admin.register(DynamicURL)
class DynamicURLAdmin(ImportExportModelAdmin):
    list_display = ('path', 'title','meta_description')



from .models import Package, PackageSummary

class PackageSummaryInline(admin.TabularInline):
    model = PackageSummary
    extra = 1

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    inlines = [PackageSummaryInline]
    list_display = ('name', 'price', 'offer_price', 'slug')
    search_fields = ('name', 'slug')

@admin.register(PackageSummary)
class PackageSummaryAdmin(admin.ModelAdmin):
    list_display = ('package', 'summary')
    search_fields = ('package__name', 'summary')