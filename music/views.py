from django.http import Http404
from .models import Album, Song
from django.shortcuts import render, get_object_or_404


def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums
    }
    return render(request, "music/index.html", context)


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except:
        raise Http404("Album does not exist")
    return render(request, "music/detail.html", {"album": album})


def favourite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST["song"])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html',
                      {'album': album, 'error_message': 'you did not select a valid song'})
    else:
        selected_song.is_favourite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})
