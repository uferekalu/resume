"""resume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

from searches.views import search_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('resumesite.urls', namespace='resumesite')),
    path('todo/', include('todo.urls', namespace='todo')),
    path('records/', include('records.urls', namespace='records')),
    path('contacts/', include('contact.urls', namespace='contact')),
    path('ecommerce/', include('ecommerce.urls', namespace='ecommerce')),
    path('search/', search_view),
    path('blog/', include('blog.urls', namespace='blogs')),
    path('blog/api/', include('blog.api.urls', namespace='blogs-api')),

    re_path(r'^cms/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'^pages/', include(wagtail_urls)),
]

if settings.DEBUG:
    #  test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)