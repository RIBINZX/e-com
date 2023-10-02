from . import views
from django.urls import path
from django.views.generic import TemplateView


app_name = "products"

urlpatterns = [
    path("", views.ProductsList.as_view(), name="products"),
    path("categories/", views.CatogoriesList.as_view(), name="categories"),
    path("subcategories/", views.SubcategoriesList.as_view(), name="subcategories"),
]
