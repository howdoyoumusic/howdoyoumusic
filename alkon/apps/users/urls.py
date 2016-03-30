from django.conf.urls import patterns, url
from django.contrib.auth.views import (
    login, logout,
    password_reset, password_reset_done,
    password_reset_confirm, password_reset_complete
    )
from django.conf import settings

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', login, name='user_login'),
    url(r'^logout/$', logout, name='user_logout'),
    url(r'^profile/$', views.user_profile_view, name='profile-detail'),
    url(r'^profile/edit/$', views.edit_profile_view, name='profile-edit'),
  )