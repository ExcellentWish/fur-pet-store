from django.contrib import admin
from .models import Review
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user','title', 'body', 'created_date', 'approved')
 
