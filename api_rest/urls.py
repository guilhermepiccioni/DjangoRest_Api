from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'Welcome', views.UserTestViewSet)
router.register(r'Profile', views.UserProfileViewset)
router.register(r'Feed', views.UserProfileFeedViewSet)


urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('api/', include(router.urls))
]
