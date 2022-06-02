from django.urls import include, path
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register(r'posts', PostsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]