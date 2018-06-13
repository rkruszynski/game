"""game URL Configuration

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

urlpatterns = [
    path('legendary/', include('legendary.urls')),
    path('create/', include('legendary.urls')),
    path('add_team/', include('legendary.urls')),
    path('teams/', include('legendary.urls')),
    path('games', include('legendary.urls')),
    path('admin/', admin.site.urls),
    path('legendary/thanks/', include('legendary.urls')),
    path('add_mastermind/', include('legendary.urls')),
    path('masterminds/', include('legendary.urls')),
    path('add_scheme/', include('legendary.urls')),
    path('schemes/', include('legendary.urls')),

]
