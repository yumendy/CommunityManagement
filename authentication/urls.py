from django.conf.urls import url
from authentication import views

urlpatterns = [
    url(r'^department/add/$', views.DepartmentCreateView.as_view(), name='department-add'),
    url(r'^department/list/$', views.DepartmentListView.as_view(), name='department-list'),
    url(r'^department/(?P<pk>[0-9]+)/update/$', views.DepartmentUpdateView.as_view(), name='department-update'),
    url(r'^department/(?P<pk>[0-9]+)/delete/$', views.DepartmentDeleteView.as_view(), name='department-delete'),

    url(r'^user/logout/$', views.LogoutView.as_view(), name='user-logout'),
    url(r'^user/login/$', views.LoginView.as_view(), name='user-login'),
    url(r'^user/apply/$', views.ApplyView.as_view(), name='user-apply'),

    url(r'^user/(?P<pk>[0-9]+)/update/$', views.UserUpdateView.as_view(), name='myuser-update'),
    url(r'^user/list/unauthorized/$', views.UnauthorizedUserListView.as_view(), name='unauthorized-user-list'),
    url(r'^user/list/member/$', views.UserListView.as_view(), name='myuser-list'),
    url(r'^user/(?P<pk>[0-9]+)/detail/$', views.UserDetailView.as_view(), name='myuser-detail'),
    url(r'^user/(?P<pk>[0-9]+)/delete/$', views.UserDeleteView.as_view(), name='myuser-delete'),
    url(r'^user/(?P<pk>[0-9]+)/authorize/$', views.AuthorizeUserView.as_view(), name='myuser-authorize'),
]
