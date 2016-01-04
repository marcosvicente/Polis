from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'core.views.index', name='index'),
    url(r'^login/', 'login.views.login', name='login'),
    url(r'^blog/', 'blog.views.blog', name='blog'),
]
