"""
URL configuration for myProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views  # Import the views module

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', views.index, name='index'),  # Add this line for the root URL
    path("", views.ones, name="ones"),
    path("analyze/", views.analyze, name="analyze"),  # Note the trailing slash
    # Add this line for the root URL
    # path('capitalizeFirst', views.capitalizeFirst, name='capitalizeFirst'),
    # path('newlineRemove', views.newlineRemove, name='newlineRemove'),
    # path('spaceRemove', views.spaceRemove, name='spaceRemove'),
    # path('charCount', views.charCount, name='charCount'),
]