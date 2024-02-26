from django.views import generic
from django.utils import timezone

from .models import Recipe

class IndexView(generic.ListView):
    template_name = "recipes/index.html"
    context_object_name = "recipe_list"

    def get_queryset(self):
        return Recipe.objects.filter(pub_date__lte=timezone.now())
    
class RecipeView(generic.DetailView):
    model = Recipe
    template_name = "recipes/recipe.html"