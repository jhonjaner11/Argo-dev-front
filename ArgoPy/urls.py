"""ArgoPy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from users import views

# Restringir url's
from django.contrib.auth.decorators import login_required

# Carga de archivos '/media/'
from django.conf import settings
from django.conf.urls.static import static

# Correo cambio de cotraseña
#from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.contrib.auth import urls
from django.contrib.auth import views

urlpatterns = [

    path('admin/', admin.site.urls),
    # ----------- URLS Módulo Usuarios ----------- #
    path('users/', include(('users.urls','users'), namespace='users')),
    path('dependences/', include(('dependences.urls','dependences'), namespace='dependences')),
    #path('accounts/', include('django.contrib.auth.urls')),

    # ----------- Iniciar sesión () ----------- #
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),
    #path('logout/', auth_views.LogoutView.as_view(template_name=''), name='logout'),
#    path('accounts/', include('django.contrib.auth.urls')),
    path('reset/', auth_views.LoginView.as_view(template_name='users/reset_pass.html'), name='reset'),
    # ----------- Registro ----------- #
    path('register_1/', auth_views.LoginView.as_view(template_name='registration/login_step1.html'), name='register_1'),
    path('register_2/', auth_views.LoginView.as_view(template_name='registration/login_step2.html'), name='register_2'),
    path('register_3/', auth_views.LoginView.as_view(template_name='registration/login_step3.html'), name='register_3'),
    path('register_4/', auth_views.LoginView.as_view(template_name='registration/login_step4.html'), name='register_4'),
] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #de static, pasame los valores de MediaRoot
