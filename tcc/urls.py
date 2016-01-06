from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'core.views.index', name='index'),
    url(r'^login/$', 'login.views.login', name='login'),
    url(r'^blog/$', 'blog.views.blog', name='blog'),
    url(r'^blog/(?P<slug>[\w-]+)/$', 'blog.views.blog_detail', name='blog_detail'),
]

if settings.DEBUG:
    urlpatterns.append(
        url(
            r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {
                'document_root': settings.MEDIA_ROOT,
                'show_indexes': True
            }
        ),
    )
