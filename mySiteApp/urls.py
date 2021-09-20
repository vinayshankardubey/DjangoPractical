from django.contrib import admin
from django.urls import path,include
from mySiteApp import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from mySiteApp.views import GameLevelViewSet

router = routers.DefaultRouter()
router.register(r'', GameLevelViewSet)

urlpatterns = [
    path('', views.image_upload_view, name = "home"),
    # path('', views.GameLevelViewSet, name = "api"),

    path('upload/', views.image_upload_view, name = "upload image"),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)