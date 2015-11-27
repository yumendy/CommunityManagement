from django.conf.urls import url
from article import views

urlpatterns = [
    url('^category/add/$', views.CategoryCreateView.as_view(), name='category-add'),
    url('^category/list/$', views.CategoryListView.as_view(), name='category-list'),
    url('^category/(?P<pk>[0-9]+)/update/$', views.CategoryUpdateView.as_view(), name='category-update'),
    url('^category/(?P<pk>[0-9]+)/delete/$', views.CategoryDeleteView.as_view(), name='category-delete')
]
