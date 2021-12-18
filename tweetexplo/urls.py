from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from api import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tweets', views.TweetListApiView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    ]

urlpatterns += router.urls


