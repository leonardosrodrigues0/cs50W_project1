from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("randompage", views.randompage, name="randompage"),
    path("newpage", views.newpage, name="newpage"),
    path("error", views.entry, name="error"),
    path("edit-<str:entry>", views.editpage, name="editpage"),
    path("<str:entry>", views.entry, name="entry")
]
