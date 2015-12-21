from django.conf.urls import url
from article import views

urlpatterns = [
    url('^category/add/$', views.CategoryCreateView.as_view(), name='category-add'),
    url('^category/list/$', views.CategoryListView.as_view(), name='category-list'),
    url('^category/(?P<pk>[0-9]+)/update/$', views.CategoryUpdateView.as_view(), name='category-update'),
    url('^category/(?P<pk>[0-9]+)/delete/$', views.CategoryDeleteView.as_view(), name='category-delete'),

    url('^blog/add/$', views.BlogCreateView.as_view(), name='blog-add'),
    url('^blog/(?P<pk>[0-9]+)/update/$', views.BlogUpdateView.as_view(), name='blog-update'),
    url('^blog/(?P<pk>[0-9]+)/delete/$', views.BlogDeleteView.as_view(), name='blog-delete'),
    url('^blog/(?P<pk>[0-9]+)/detail/$', views.BlogDetailView.as_view(), name='blog-detail'),
    url('^blog/list/all/$', views.BlogListView.as_view(), name='blog-list'),
    url('^blog/list/personal/$', views.PersonalBlogListView.as_view(), name='blog-list-personal'),

    url('^pure_page/add/$', views.PurePageCreateView.as_view(), name='pure-page-add'),
    url('^pure_page/(?P<pk>[0-9]+)/update/$', views.PurePageUpdateView.as_view(), name='pure-page-update'),
    url('^pure_page/(?P<pk>[0-9]+)/delete/$', views.PurePageDeleteView.as_view(), name='pure-page-delete'),
    url('^pure_page/(?P<pk>[0-9]+)/detail/$', views.PurePageDetailView.as_view(), name='pure-page-detail'),
    url('^pure_page/list/personal/$', views.PurePageListView.as_view(), name='pure-page-list'),

]
