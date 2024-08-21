from django.urls import path
from .views import homView,NewsView, kataktWiev,jahonWiev,sportWiev

urlpatterns=[
    path("",homView,name="sahifa"),
    path("new/",NewsView,name="yangilik"),
    path("www/",kataktWiev,name="sahifaa"),
    path("neww/",jahonWiev,name="jahon"),
    path("neee/",sportWiev,name="sport"),
]