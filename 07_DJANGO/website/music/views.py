from django.http import HttpResponse
from django.http import Http404
from django.template import loader  # Can use django.shortcut instead
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# CreateView is a form to create a new object
# UpdateView is a form to modify an object
# DeleteView is a from to delete an object
#from django.contrib.auth import authenticate, login
#from django.contrib.auth import logout
#from django.http import JsonResponse
#from django.db.models import Q
from .forms import AlbumForm, SongForm, UserForm
from .models import Album, Song

AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

# Create your views here. Better to keep the html to the templates


# Original Album details page
def detail1(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return HttpResponse("<h2>Album Details for Album id: " + str(album_id) + " </h2>")

# Used Templates
def detail2(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    context = {'album' : album}
    return render(request, 'music\detail2.html', context)

# Used Templates and shortcu
def detail3(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    context = {'album' : album}
    return render(request, 'music\detail2.html', context)


# Original Index Page
def index1(request):
    all_albums = Album.objects.all()
    html = "<h1>TSC App Homepage</h1>"
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html)

# Used Templates instead
def index2(request):
     all_albums = Album.objects.all()
     template = loader.get_template('music\index2.html') # looks in template directory
     context = {'all_albums':all_albums,}
     return HttpResponse(template.render(context,request))

# Used Shortcut template method
def index3(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music\index2.html', context)

def favorite2(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {'album':album, 'error_message': "You did not select a valid song"})
    else:
        selected_song.is_favorite = True
        selected_song.save()
    context = {'album' : album}
    return render(request, 'music\detail2.html', context)


# Genereric View examples use classes not functions
class IndexView(generic.ListView):
    template_name = 'music/index2.html'
    context_object_name = 'all_albums' # otherwise you would need to refer to all_albums as 'object_list' in templates which is the built-in name
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail2.html'

class SongsListView(generic.ListView):
    model = Song

# GOOD WAY TO CREATE ALBUM
class AlbumCreate(CreateView):
    model = Album
    fields=['artist', 'album_title','genre', 'album_logo']  # list all the input fields for the model

class AlbumUpdate(UpdateView):
    model = Album
    fields=['artist', 'album_title','genre', 'album_logo']  # list all the input fields for the model

class AlbumDelete(DeleteView):
    model = Album
    fields=['artist', 'album_title','genre', 'album_logo']  # list all the input fields for the model
    success_url = reverse_lazy('music:index2')  # Redirect on delete

# BAD WAY TO CREATE ALBUM
def create_album(request):
    if False: # not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        form = AlbumForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.album_logo = request.FILES['album_logo']
            file_type = album.album_logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'album': album,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'music/create_album.html', context)
            album.save()
            return render(request, 'music/detail.html', {'album': album})
        context = {
            "form": form,
        }
        return render(request, 'music/create_album.html', context)







# def create_song(request, album_id):
#     form = SongForm(request.POST or None, request.FILES or None)
#     album = get_object_or_404(Album, pk=album_id)
#     if form.is_valid():
#         albums_songs = album.song_set.all()
#         for s in albums_songs:
#             if s.song_title == form.cleaned_data.get("song_title"):
#                 context = {
#                     'album': album,
#                     'form': form,
#                     'error_message': 'You already added that song',
#                 }
#                 return render(request, 'music/create_song.html', context)
#         song = form.save(commit=False)
#         song.album = album
#         song.audio_file = request.FILES['audio_file']
#         file_type = song.audio_file.url.split('.')[-1]
#         file_type = file_type.lower()
#         if file_type not in AUDIO_FILE_TYPES:
#             context = {
#                 'album': album,
#                 'form': form,
#                 'error_message': 'Audio file must be WAV, MP3, or OGG',
#             }
#             return render(request, 'music/create_song.html', context)
#
#         song.save()
#         return render(request, 'music/detail.html', {'album': album})
#     context = {
#         'album': album,
#         'form': form,
#     }
#     return render(request, 'music/create_song.html', context)
#
#
# def delete_album(request, album_id):
#     album = Album.objects.get(pk=album_id)
#     album.delete()
#     albums = Album.objects.filter(user=request.user)
#     return render(request, 'music/index.html', {'albums': albums})
#
#
# def delete_song(request, album_id, song_id):
#     album = get_object_or_404(Album, pk=album_id)
#     song = Song.objects.get(pk=song_id)
#     song.delete()
#     return render(request, 'music/detail.html', {'album': album})
#
#
# def detail(request, album_id):
#     if False: # not request.user.is_authenticated():
#         return render(request, 'music/login.html')
#     else:
#         user = request.user
#         album = get_object_or_404(Album, pk=album_id)
#         return render(request, 'music/detail.html', {'album': album, 'user': user})
#
#
# def favorite(request, song_id):
#     song = get_object_or_404(Song, pk=song_id)
#     try:
#         if song.is_favorite:
#             song.is_favorite = False
#         else:
#             song.is_favorite = True
#         song.save()
#     except (KeyError, Song.DoesNotExist):
#         return JsonResponse({'success': False})
#     else:
#         return JsonResponse({'success': True})
#
#
# def favorite_album(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         if album.is_favorite:
#             album.is_favorite = False
#         else:
#             album.is_favorite = True
#         album.save()
#     except (KeyError, Album.DoesNotExist):
#         return JsonResponse({'success': False})
#     else:
#         return JsonResponse({'success': True})
#
#
# def index(request):
#     if False:  # not request.user.is_authenticated():
#         return render(request, 'music/login.html')
#     else:
#         albums = Album.objects.filter(user=request.user)
#         song_results = Song.objects.all()
#         query = request.GET.get("q")
#         if query:
#             albums = albums.filter(
#                 Q(album_title__icontains=query) |
#                 Q(artist__icontains=query)
#             ).distinct()
#             song_results = song_results.filter(
#                 Q(song_title__icontains=query)
#             ).distinct()
#             return render(request, 'music/index.html', {
#                 'albums': albums,
#                 'songs': song_results,
#             })
#         else:
#             return render(request, 'music/index.html', {'albums': albums})
#
#
# def logout_user(request):
#     logout(request)
#     form = UserForm(request.POST or None)
#     context = {
#         "form": form,
#     }
#     return render(request, 'music/login.html', context)
#
#
# def login_user(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 albums = Album.objects.filter(user=request.user)
#                 return render(request, 'music/index.html', {'albums': albums})
#             else:
#                 return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
#         else:
#             return render(request, 'music/login.html', {'error_message': 'Invalid login'})
#     return render(request, 'music/login.html')
#
#
# def register(request):
#     form = UserForm(request.POST or None)
#     if form.is_valid():
#         user = form.save(commit=False)
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         user.set_password(password)
#         user.save()
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 albums = Album.objects.filter(user=request.user)
#                 return render(request, 'music/index.html', {'albums': albums})
#     context = {
#         "form": form,
#     }
#     return render(request, 'music/register.html', context)
#
#
# def songs(request, filter_by):
#     if False: # not request.user.is_authenticated():
#         return render(request, 'music/login.html')
#     else:
#         try:
#             song_ids = []
#             for album in Album.objects.filter(user=request.user):
#                 for song in album.song_set.all():
#                     song_ids.append(song.pk)
#             users_songs = Song.objects.filter(pk__in=song_ids)
#             if filter_by == 'favorites':
#                 users_songs = users_songs.filter(is_favorite=True)
#         except Album.DoesNotExist:
#             users_songs = []
#         return render(request, 'music/songs.html', {
#             'song_list': users_songs,
#             'filter_by': filter_by,
#         })

