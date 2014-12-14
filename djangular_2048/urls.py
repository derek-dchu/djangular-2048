from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', include('game.urls', namespace='game-app', app_name="game")),
    url(r'^admin/', include(admin.site.urls)),
)