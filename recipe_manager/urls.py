"""recipe_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path
from .views import home_view
from articles.views import (
    article_create_view,
    article_detail_view,
    article_search_view
)
from accounts.views import (
    login_view
)

urlpatterns = [
    path('', home_view), #index
    path('articles/', article_search_view),
    path('articles/create/', article_create_view),
    path('articles/<int:id>/', article_detail_view),
    # re_path(r'articles/(?P<id>\d+)/$', home_view) // older versions
    path('admin/', admin.site.urls),
    path('login/', login_view)
]
