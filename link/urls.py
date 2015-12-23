from django.conf.urls import url
from link import views

urlpatterns = [
    url(r'^add/$', views.LinkCreateView.as_view(), name='link-add'),
    url(r'^list/$', views.LinkListView.as_view(), name='link-list'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.LinkUpdateView.as_view(), name='link-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.LinkDeleteView.as_view(), name='link-delete'),
]
