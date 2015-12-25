from django.conf.urls import url
from activity import views

urlpatterns = [
    url(r'^actor/(?P<activity_id>[0-9]+)/add/$', views.ActorCreateView.as_view(), name='actor-add'),
    url(r'^actor/(?P<activity_id>[0-9]+)/list/$', views.ActorListView.as_view(), name='actor-list'),
    url(r'^actor/(?P<pk>[0-9]+)/delete/$', views.ActorDeleteView.as_view(), name='actor-delete'),

    url(r'^task/add/$', views.TaskCreateView.as_view(), name='task-add'),
    url(r'^task/list/$', views.TaskListView.as_view(), name='task-list'),
    url(r'^task/(?P<pk>[0-9]+)/update/$', views.TaskUpdateView.as_view(), name='task-update'),
    url(r'^task/(?P<pk>[0-9]+)/delete/$', views.TaskDeleteView.as_view(), name='task-delete'),
    url(r'^task/(?P<pk>[0-9]+)/detail/$', views.TaskDetailView.as_view(), name='task-detail'),

    url(r'^activity/add/$', views.ActivityCreateView.as_view(), name='activity-add'),
    url(r'^activity/list/$', views.ActivityListView.as_view(), name='activity-list'),
    url(r'^activity/(?P<pk>[0-9]+)/update/$', views.ActivityUpdateView.as_view(), name='activity-update'),
    url(r'^activity/(?P<pk>[0-9]+)/delete/$', views.ActivityDeleteView.as_view(), name='activity-delete'),
    url(r'^activity/(?P<pk>[0-9]+)/detail/$', views.ActivityDetailView.as_view(), name='activity-detail'),
]
