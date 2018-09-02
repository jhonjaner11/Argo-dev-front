from django.urls import path, re_path

from . import views
urlpatterns = [
    path('new', views.new_dependence, name='new'),
    path('all',views.list_dependences, name='list'),
    path('search',views.search_dependences, name='search'),
    path('delete/<int:id_dependence>/',views.delete_dependence, name='delete'),
    path('edit/<int:id_dependence>/',views.edit_dependence, name='edit'),
    ]
