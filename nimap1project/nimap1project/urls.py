"""nimap1project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert/',views.insertuser),
    path('userinfo/', views.userinfo_view),
    path('insertclient/', views.insertclient),
    path('clientinfo/', views.clientinfo_view),
    path('userinfo/delete/<int:id>/',views.deleteuser),
    path('userinfo/update/<int:id>/',views.updateuserview),
    path('clientinfo/delete/<int:id>/',views.deleteclient),
    path('clientinfo/update/<int:id>/',views.updateclientview)

]


