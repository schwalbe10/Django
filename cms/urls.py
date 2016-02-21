from django.conf.urls import patterns, url
from cms import views

urlpatterns = [
    url(r'^record/$', views.record_list, name='record_list'),     # List
    url(r'^record/add/$', views.record_edit, name='record_add'),  # Add
    url(r'^record/mod/(?P<record_id>\d+)/$', views.record_edit, name='record_mod'),  # Edit
    url(r'^record/del/(?P<record_id>\d+)/$', views.record_del, name='record_del'),   # Delete

    url(r'^review/(?P<record_id>\d+)/$', views.ReviewList.as_view(), name='review_list'),  # List
    url(r'^review/add/(?P<record_id>\d+)/$', views.review_edit, name='review_add'),        # Add
    url(r'^review/mod/(?P<record_id>\d+)/(?P<review_id>\d+)/$', views.review_edit, name='review_mod'),  # Edit
    url(r'^review/del/(?P<record_id>\d+)/(?P<review_id>\d+)/$', views.review_del, name='review_del'),   # Delete
]
