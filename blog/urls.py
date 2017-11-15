from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk_var>\d+)/$', views.post_detail, name='post_detail_name'),
    url(r'^post/(?P<pk_req_var>\d+)/edit/$', views.post_edit, name='post_edit_name'),
    url(r'^post/new/$', views.post_new, name='post_new'),
]