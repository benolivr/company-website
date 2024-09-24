from django.urls import path

from .views import homePageView, AboutPageView, ProductsPageView      

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("products/", ProductsPageView.as_view(), name="products"),
    path("", homePageView, name="home")
]       