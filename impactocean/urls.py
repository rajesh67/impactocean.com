"""impactocean URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from apps.webapp.views import home,contact

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls', namespace='blog')),

    # provide the most basic login/logout functionality
    url(r'^$', home, name='home'),
    url(r'^contact/$', contact, name="contact"),

    # enable the admin interface
    url(r'^admin/', admin.site.urls),
]
