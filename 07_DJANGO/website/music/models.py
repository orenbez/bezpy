from django.db import models
#from django.core.urlresolvers import reverse  @ wasn't here
from django.shortcuts import reverse
from datetime import datetime as dt

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=150)
    album_title = models.CharField(max_length=150)
    genre = models.CharField(max_length=150)
    album_logo = models.FileField()
    created_at = models.DateTimeField(default=dt.now, blank=True)

    def get_absolute_url(self):
        return reverse('music:detail4', kwargs={'pk': self.pk})  # Returns '/music/gv_detail/<pk>/'

    def __str__(self):   # String representation for an album used by e.g. print() command
        return f"PK: {self.pk}, Artist: {self.artist}, Title: {self.album_title}"


class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE) #foreign key must exist if Album deleted all of songs also will delete
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=200)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)
    def __str__(self):
        return f"PK: {self.pk}, Song: {self.song_title}"

# MIGRATION
# python manage.py makemigrations <class_name>   # have option to specify the table/class
# python manage.py migrate <class_name>          # have option to specify the table/class

# COMMANDS FOR THE SHELL
# from music.models import Album, Song

# ======Add Album by Constructer =======================================================================================
# a1 = Album(artist='Beatles', album_title='Abbey Road', genre='rock', album_logo='file1.jpg')  # CREATE INSTANCE
# a1 = Album()  # or you can create instance first and then populate the values ...  a1.artist='Beatles'
# a1.save()             # Required to save to db otherwise changes will only exist in the shell
# a1.id                 # Returns the incremented id value, also use a.pk
# a1.genre               # displays the genre



# ======================================================================================================================
# Album.objects.all()  # displays all of the records, uses __str__ if defined in the Class function
# Album.objects.all().delete()  # deletes all objects of type album
# all_albums = Album.objects.all()  # assigns full collection of Album objects as Query Set
# all_albums[0].album_title     # Returns title of first Album
# a1 = Album.objects.get(pk=1)  # Returns Album instance
# al = Album.objects.all()[0]   # Same as above returns 1st Album instance
# a1 = get_object_or_404(Album, pk=1)  #Returns Album or 404 error

# a2 = Album.objects.get(pk=2)  # Assigns a2 which is of type Album
# s1 = Song(album=a2, file_type='mp3', song_title='Mysterious Ways')  # CREATE SONG
# s1.save()

# Album.objects.filter(id=1)     # displays first album - Warning: this is of type QuerySet, not Album
# Album.objects.filter(id=1)[0]  # Returns 1st Album Object that matched the filter

# Album.???.filter(id=1)     # Returns object but will give error if condition filters more than one object

# Album.objects.filter(artist__startswith='Bea')  # Uses string command for filter, returns type QuerySet
# a1.song_set.all()  # Returns QuerySet of all of 'a1's songs
# a2.song_set.all()     -- returns all songs in album a2 as QuerySet. Note: song_set is built in operator for Class 'Song'
# a2.song_set.count()   -- returns count of songs in album a2
# a2.song_set.create(song_title='One', file_type='mp3') -- this will create and save a new song in album a2
# s3 = a2.song_set.create(song_title='Zoo Station', file_type='mp3')   # will also return object of type Song
# s1 = a1.song_set.get(pk=1) # Returns Song with pk=1 of 1st Album if exists else gives error
# Albums.objects.order_by("-artist","album_title")  equivalent to  ORDER BY artist DESC, album_title ASC
