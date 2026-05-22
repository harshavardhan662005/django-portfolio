from django.contrib import admin
from .models import Project

# This tells the admin layout exactly what text boxes to show
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'tech_stack')  # <-- These match your models.py fields