from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

# Restringir url's
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('home/', views.home, name='home'),
    path('person/new',views.new_person, name='new_person'),
    path('person/all',views.list_persons, name='list_person'),
    path('person/search',views.search_persons, name='search_person'),
    path('person/edit/<int:id_person>',views.edit_person, name='edit_person'),
    path('person/delete/<int:id_person>',views.delete_person, name='delete_person'),
] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
