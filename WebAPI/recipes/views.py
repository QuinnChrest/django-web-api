import json
from datetime import date, datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.forms.models import model_to_dict
from django.views import generic
from django.utils import timezone

from .models import Recipe

def index(request):
    data = Recipe.objects.all().values()
    json_data = json.dumps(list(data), default=json_serial)
    return HttpResponse(json_data, content_type='application/json')
    
def recipe(request, recipe_id):
    data = get_object_or_404(Recipe, pk=recipe_id)
    json_data = json.dumps(model_to_dict(data), default=json_serial)
    return HttpResponse(json_data, content_type='application/json')

def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

# class IndexView(generic.ListView):
#     template_name = "recipes/index.html"
#     context_object_name = "recipe_list"

#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Recipe.objects.filter(pub_date__lte=timezone.now())

# class RecipeView(generic.DetailView):
#     model = Recipe
#     template_name = "recipes/recipe.html"

# def index(request):
#     recipe_list = Recipe.objects.filter(pub_date__lte=timezone.now())
#     context = {"recipe_list": recipe_list}
#     return render(request, "recipes/index.html", context)

# def recipe(request, recipe_id):
#     recipe = get_object_or_404(Recipe, pk=recipe_id)
#     context = {"recipe": recipe}
#     return render(request, "recipes/recipe.html", context)