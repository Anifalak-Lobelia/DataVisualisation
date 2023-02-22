# 21122924 刘育杰 智能科学与技术
"""Project URL Configuration
URL和函数的对应关系
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
from app01 import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    #www.xxx.com/index  -> 函数
    path('',views.login),
    path('choose/',views.choose),
    path('shengxiao/',views.shengxiao),
    path('jieqi/',views.jieqi),
]
