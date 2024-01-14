"""FavoriteTunes URL Configuration

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
from TuneTracker import views
from . import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('songs/',views.display_songs, name = 'songs_list'),
    path('artists/',views.display_artists, name = 'artists_list'),
    path('songs/<int:song_id>/', views.display_song_detail, name = 'song_detail'),
    path('add_song/', views.add_song, name='add_song'),
    path('add_artist/',views.add_artist,name='add_artist')
]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
