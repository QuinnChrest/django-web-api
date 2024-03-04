from django.urls import path

from . import views

app_name = "recipes"
urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("<int:recipe_id>/", views.recipe, name="recipe"),
]