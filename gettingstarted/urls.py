"""
URL configuration for gettingstarted project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path

import hello.views

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("translate/", hello.views.translate, name="translate"),
    path("translatePhoto/", hello.views.translatePhoto, name="translatePhoto"),
    path("sendPhoto/", hello.views.sendPhoto, name="sendPhoto"),
    path("viewTranslatePhoto/", hello.views.viewTranslatePhoto, name="viewTranslatePhoto"),
    path("sendPhotoAndView/", hello.views.sendPhotoAndView, name="sendPhotoAndView"),
    path("extractText", hello.views.extractText, name="extractText"),
    path("extractTextByAudio", hello.views.extractTextByAudio, name="extractTextByAudio"),
    # path("extractTextByAudio64", hello.views.extractTextByAudio64, name="extractTextByAudio64"),
    # Uncomment this and the entry in `INSTALLED_APPS` if you wish to use the Django admin feature:
    # https://docs.djangoproject.com/en/4.2/ref/contrib/admin/
    # path("admin/", admin.site.urls),
]
