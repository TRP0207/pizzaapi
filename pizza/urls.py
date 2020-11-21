from django.urls import path
from . import views
urlpatterns = [
    path('pizza/', views.PizzaList.as_view()),
    path('pizza/<int:pk>/',views.PizzaDetail.as_view()),
   
]



