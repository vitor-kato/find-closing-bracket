from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import find_closing_bracket_list
from .views import find_closing_bracket_detail


urlpatterns = {
    url(r'^api/v1/bracket/$', find_closing_bracket_list, name="create"),
    url(r'^api/v1/bracket/(?P<pk>[0-9]+)/$',
        find_closing_bracket_detail, name="detail"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
