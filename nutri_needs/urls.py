from django.urls import path
from . import views


urlpatterns = [
    path("",views.nutri_need_home,name="nutri_need_home"),
     path("about/",views.nutri_need_about,name="nutri_need_about"),
]
