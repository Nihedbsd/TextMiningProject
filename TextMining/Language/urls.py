from django.conf.urls import url, include
from django.urls import path
from .views import FileView
from . import views  # import views so we can use them in urls.
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'upload', FileView, 'upload')


app_name = 'Language'

urlpatterns = [


    # url(r'^', include(router.urls), name='lango'),
    url(r'^upload/$', FileView.as_view(), name='file-upload'),
    url(r'^upload/(?P<filename>[^/]+)$', FileView.as_view(), name='upload')
]
