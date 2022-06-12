from django.urls import include, path
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register(r'posts', PostsViewSet)

popularRouter = routers.DefaultRouter()
popularRouter.register(r'post', PopularPostViewSet, basename='popularSet')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(popularRouter.urls)),
]