from django.conf.urls import url
from announcement import views

urlpatterns = [
    url(r'^add/$', views.AnnouncementCreateView.as_view(), name='announcement-add'),
    url(r'^list/$', views.AnnouncementListView.as_view(), name='announcement-list'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.AnnouncementUpdateView.as_view(), name='announcement-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.AnnouncementDeleteView.as_view(), name='announcement-delete'),
]
