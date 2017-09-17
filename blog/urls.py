from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.Indexview.as_view(), name='index'),
url(r'^logout/$', views.logout_view, name='logout'),
url(r'^register/$', views.UserFormView.as_view(), name='register'),
url(r'^signin/$', views.SignInView.as_view(), name='sign-in'),
url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name ='detail'),
url(r'^post/add/$', views.PostCreate.as_view(), name='post-add'),
]
