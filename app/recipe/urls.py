"""
URL mappings for the recipe app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)
router.register('tag',views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)

app_name = 'recipe'#This is used when we want to used revses function

urlpatterns = [
    path('', include(router.urls)),
]