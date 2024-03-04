import json
from datetime import date, datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.forms.models import model_to_dict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from django.utils import timezone

from .models import Recipe

def index(request):
    recipes = Recipe.objects.all()
    paginator = Paginator(recipes,1)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(paginator.num_pages)
    data = [model_to_dict(recipe) for recipe in page_obj.object_list]
    payload = {
        "page": {
            "current": page_obj.number,
            "has_next": page_obj.has_next(),
            "has_previous": page_obj.has_previous(),
            "count": paginator.num_pages
        },
        "recipes": data
    }
    return JsonResponse(payload)

def search(request):
    search  = request.GET.get('search')
    recipes = Recipe.objects.filter(title__contains=search)
    paginator = Paginator(recipes,1)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(paginator.num_pages)
    data = [model_to_dict(recipe) for recipe in page_obj.object_list]
    payload = {
        "page": {
            "current": page_obj.number,
            "has_next": page_obj.has_next(),
            "has_previous": page_obj.has_previous(),
            "count": paginator.num_pages
        },
        "recipes": data
    }
    return JsonResponse(payload)
    
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