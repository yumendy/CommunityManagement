from django.conf.urls import url
from carousel import views

urlpatterns = [
    url(r'^add/$', views.CarouselCreateView.as_view(), name='carousel-add'),
    url(r'^list/$', views.CarouselListView.as_view(), name='carousel-list'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.CarouselUpdateView.as_view(), name='carousel-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.CarouselDeleteView.as_view(), name='carousel-delete'),
]
