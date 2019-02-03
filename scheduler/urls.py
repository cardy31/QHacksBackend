from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as rest_views
from scheduler import views

urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^api-token-auth/', rest_views.obtain_auth_token, name='token-get'),
    url(r'^scheduler/$', views.SchedulerList.as_view(), name='scheduler-list'),
    url(r'^scheduler/(?P<pk>[0-9]+)/$', views.SchedulerDetail.as_view(), name='scheduler-detail'),
    url(r'^user/$', views.UserList.as_view(), name='user-list'),
    url(r'^googlehome/$', views.GoogleHomeEndpoint.as_view(), name='google-home'),
    url(r'^s/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
])
