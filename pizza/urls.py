from django.urls import path
from . import views
urlpatterns = [
    path('pizza/', views.PizzaList.as_view()),
    path('pizza/<int:pk>/',views.PizzaDetail.as_view()),
    # path('<str:shape>/<str:size>', views.SpesList.as_view()),
    # path('<size>', views.SpeList.as_view()),
]



"""
hi  bol thae gayu call upad bije call hale hai to mne smjavu to pdse j karnke bharthi no call aayvo to bharathi na call ne aane shu lage vadge
are kalno baapu koina caal upadto nthi msg na ans nthi aapto kapi nakhe he phone
are ane ne samjavane shu lage vadge
hal e bdhu may gyu aa kr
bapa vat kare chhe
are easy j chhe
filtering by parameters j karyu chhe
jo aa documentaesion ma


http://127.0.0.1:8000/pizza/ aa url par badha pizza aavya
have queryset parameter pass karvana

"""
