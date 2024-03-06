from django.urls import path, re_path

from . import views

app_name = "recipes"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:recipe_id>/", views.recipe, name="recipe"),
    path("search/", views.search, name="search"),
    path("add", views.add, name="add"),
    re_path('login', views.login),
]