from django.conf.urls import patterns, include, url
from django.contrib import admin

import testapp.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'select2_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^/?', include(testapp.urls)),
)
