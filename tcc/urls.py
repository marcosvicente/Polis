from django.conf.urls import include, url
from django.contrib import admin

from blog.views import BlogList 

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'core.views.index', name='index'),
    url(r'^login/', 'login.views.login', name='login'),
    url(r'^blog/', BlogList.as_view(), name='blog'),
    url(r'^blog/(?P<slug>[\w-]+)/$','blog.views.blog_post' , name="detail"),
]
