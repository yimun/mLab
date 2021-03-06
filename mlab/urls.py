#! coding=utf8

"""mlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from material.frontend import urls as frontend_urls
from django.views.generic import RedirectView
from storage.views import wangEditor_file_upload
from mlab import settings
from cms.views import tasklog, not_support, download_approve

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/home/')),
    url(r'', include(frontend_urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^wangupload/$', wangEditor_file_upload),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^tasklog/$', tasklog),
    url(r'^not_support/$', not_support),
    url(r'^download_approve/$', download_approve),

]
