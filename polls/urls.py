from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^p$', views.Index.as_view(), name='index2'),
    url(r'^p/(?P<pk>\d+)$', views.Detail.as_view(), name='index-detail'),
    url(r'^f$', views.EmailView.as_view(), name='email-detail'),
    url(r'^n$', views.NewAlbum.as_view(), name='new-album'),

]