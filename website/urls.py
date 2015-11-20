from django.conf.urls import url, include
from website import views

urlpatterns = [
    url(r'^index/$', views.IndexView.as_view(), name='index_page'),
    url(r'^$', views.HomepageView.as_view(), name='home_page'),
    url(r'^dashboard/$', views.DashboardOverviewView.as_view(), name='dashboard'),
]
