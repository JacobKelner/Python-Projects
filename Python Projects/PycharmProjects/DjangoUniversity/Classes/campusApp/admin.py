
from django.contrib import admin
from .models import UniversityCampus

# Register your models here.
admin.site.register(UniversityCampus)  # Allows for models to be added to the Django admin to create, delete, update, etc.
