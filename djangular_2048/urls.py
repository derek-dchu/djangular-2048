from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', include('game.urls', namespace='game-app', app_name="game")),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^social/', include('social.apps.django_app.urls', namespace='social', app_name='python-social-auth')),
)