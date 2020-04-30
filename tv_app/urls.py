from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('newshow', views.newshow),
    path('shows2/<id>', views.shows2),
    path('delete_show_on_list/<id>/destroy', views.delete_show_on_list),
    path('edit/<id>', views.edit),
    path('edit_show/<id>', views.edit_show)
]