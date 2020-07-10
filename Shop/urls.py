from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="Shop Home"),
    path('about/',views.about,name="About Us"),
    path('search/',views.search,name="Search"),
    path("product/<int:myid>", views.productview, name="Product View"),
    path('checkout/',views.checkout,name="Check Out"),

]
