from django.conf.urls import url
from . import views  # means import views modules from current directory

app_name = 'music'  # this defines namespace for the template references like {% url 'music:detail1' album.id %}

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^register/$', views.register, name='register'),
    # url(r'^login_user/$', views.login_user, name='login_user'),
    # url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^d1/(?P<album_id>[0-9]+)/$', views.detail1, name='detail1'),
    # url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    #url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    # url(r'^create_album/$', views.create_album, name='create_album'),
    # url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    # url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    # url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    # url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),

    url(r'^$', views.index3, name='index3'),                           # /music/
    url(r'^index2/$', views.index2, name='index2'),                    # /music/index2/
    url(r'^index1/$', views.index1, name='index1'),                    # /music/index1/
    url(r'^gv_index$', views.IndexView.as_view(), name='index4'),       # /music/gv_index/

    url(r'^(?P<album_id>[0-9]+)/$', views.detail3, name='detail3'),                   # /music/712/    ?P<album_id>  will extract the digits entered and store as album_id when accessing the view
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite2, name='favorite'),        # /music/712/favorite
    url(r'^gv_detail/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail4'),   # /music/gv_detail/712/    ?P<album_id>  will extract the digits entered and store as album_id when accessing the view
    url(r'^album/add/$', views.create_album, name='album-add'),                         # /music/album/add
    url(r'^gv_album/add/$', views.AlbumCreate.as_view(), name='gv_album-add'),          # /music/gv_album/add
    url(r'^gv_album/update/(?P<pk>[0-9]+)$', views.AlbumUpdate.as_view(), name='gv_album-update'),  # /music/gv_album/update/2/
    url(r'^gv_album/delete/(?P<pk>[0-9]+)$', views.AlbumDelete.as_view(), name='album-delete'),
    url(r'^songs/$', views.SongsListView.as_view(), name='songs'),                       # /music/songs/
]
