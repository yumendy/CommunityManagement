from django.conf.urls import url, include
from website import views

urlpatterns = [
    url(r'^index/$', views.IndexView.as_view(), name='index_page'),
    url(r'^$', views.HomepageView.as_view(), name='homepage'),
    url(r'^dashboard/$', views.DashboardOverviewView.as_view(), name='dashboard'),
    url(r'^settings/$', views.SettingsOverviewView.as_view(), name='settings'),
]
