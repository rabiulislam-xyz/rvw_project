from django.conf.urls import url

from blog import views


app_name = 'blog'

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='post_list'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^(?P<slug>[^/]+)/$', views.PostDetail.as_view(), name='post_detail'),
]