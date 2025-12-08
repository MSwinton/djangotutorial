from django.urls import path

from rolls import views

urlpatterns = [
    path("", views.index, name="index")
]