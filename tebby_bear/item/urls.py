from django.urls import path

from . import views

app_name = "item"

urlpatterns = [
    path('', views.items, name="items"),
    path("new_tebby/", views.new_tebby, name="new_tebby"),
    path("<int:pk>", views.detail, name="detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/edit/", views.edit, name="edit"),
]
