from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index,name='index' ),
    url(r'^retrieve/$',views.retrieve,name="retrieve"),
    url(r'^contact/$',views.contact,name="contact"),
    url(r'^about/$',views.about,name="about"),
    url(r'^plants/$',views.plants,name="plants"),
    url(r'^plants/(?P<plant_id>[0-9]+)/(?P<index>[0-9]+)/$',views.common,name="common"),
]
