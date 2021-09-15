"""crud URL Configuration

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
from django.urls import path
import blog.views
import account.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.main, name='main'),
    path('detail/<str:id>', blog.views.detail, name='detail'),
    path('read/', blog.views.read, name = 'read'),
    path('new/create/', blog.views.create, name='create'),
    path('edit/<str:id>', blog.views.edit, name='edit'),
    path('delete/<str:id>', blog.views.delete, name='delete'),
    path('hashtag/', blog.views.hashtagform, name='hashtag'),
    path('search/<int:hashtag_id>/', blog.views.search, name='search'),
    path('signup/', account.views.signup, name='signup'),
    path('login/', account.views.login, name='login'),
    path('logout/', account.views.logout, name='logout'),
]
