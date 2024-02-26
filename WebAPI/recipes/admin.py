from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Recipe

admin.site.register(Recipe, MarkdownxModelAdmin)
