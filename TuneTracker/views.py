from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Song,Artist
from .forms import songForm,artistForm


# Create your views here.

def add_song(request):
    form = songForm(request.POST ,request.FILES or None)
    
    if request.method == "POST":        
        if form.is_valid():
            form.save()
            return redirect('songs_list')
        else:
            form = songForm()
    
    return render(request, 'add_songs.html', {'form': form})

def add_artist(request):
    form = artistForm(request.POST ,request.FILES or None)
    
    if request.method == "POST":        
        if form.is_valid():
            form.save()
            return redirect('artists_list')
        else:
            form = artistForm()
    return render(request, 'add_artists.html', {'form': form})

def display_songs(request):
    songs = Song.objects.all()
    return render(request, 'songs_list.html',{'songs' : songs})

def display_artists(request):
    artists = Artist.objects.all()
    return render(request, 'artists_list.html',{'artists' : artists})

def display_song_detail(request, song_id):
    song = Song.objects.get(pk=song_id)
    return render(request, 'song_detail.html', {'song': song})