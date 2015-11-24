from django.conf.urls import url
from navbar import views

urlpatterns = [
    url(r'^add/$', views.NavbarCreateView.as_view(), name='navbar-add'),
    url(r'^list/$', views.NavbarListView.as_view(), name='navbar-list'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.NavbarUpdateView.as_view(), name='navbar-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.NavbarDeleteView.as_view(), name='navbar-delete'),
]
