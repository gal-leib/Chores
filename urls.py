from django.conf.urls.defaults import patterns, include, url
from chores.views import CompleteChoreView
from chores.models import Player
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'chores.views.home', name='home'),
    url(r'^complete/$', login_required(CompleteChoreView.as_view()), name='complete_chore_view'),
    url(r'^people/(?P<pk>\d+)/$', DetailView.as_view(model=Player, template_name='player_detail.html'), name='player_view'),
    # url(r'^chores/', include('chores.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
