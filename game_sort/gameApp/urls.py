from gameApp import views
from django.conf.urls import url
urlpatterns=[
        url(r'^putscore/$',views.putsource),
        url(r'^getrank/$',views.getrank)
        ]
