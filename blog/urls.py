from django.urls import path
from . import views
from .views import SignUpView, ActivateAccount, ProfileView

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
]