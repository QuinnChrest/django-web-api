import datetime
from typing import Any
from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    source = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    description = models.CharField(max_length=400, blank=True)
    recipe = MarkdownxField()

    def formatted_markdown(self):
        return markdownify(self.recipe)

    def __str__(self) -> str:
        return self.title