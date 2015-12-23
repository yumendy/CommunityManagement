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

]
