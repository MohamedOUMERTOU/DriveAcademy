from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
router.register(r'series', views.SeriesViewSet)
router.register(r'progress', views.StudentProgressViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('api/', include(router.urls)),  # Routes for viewsets
]




