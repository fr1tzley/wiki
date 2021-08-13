from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new_page", views.new_page, name="new_page"),
    path("/new_page/add", views.add_page, name="add_page"),
    path("overlap_error", views.overlap_error, name="overlap_error"),
    path("^search/$", views.search, name="search"),
    path("random", views.random, name="random"),
    path("<str:title>", views.page, name="page"), 
    path("<str:title>/edit", views.edit, name="edit"),
    path("<str:title>/edit/confirm", views.confirm_edit, name="confirm_edit"),
]
    
