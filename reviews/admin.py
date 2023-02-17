from django.contrib import admin
from .models import  Review
from django_summernote.admin import SummernoteModelAdmin





@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user','title', 'body', 'created_date', 'approved')
    list_filter = ('approved', 'created_date')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
