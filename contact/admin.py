from django.contrib import admin
from .models import Comment, message

# Register your models here.
admin.site.register(Comment)
admin.site.register(message)