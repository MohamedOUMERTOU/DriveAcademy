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



""" from django.urls import path
from . import views

urlpatterns = [
    # URL for listing all series
    path('series/', views.SeriesListView.as_view(), name='series-list'),
    
    # URL for viewing a single series details
    path('series/<int:pk>/', views.SeriesDetailView.as_view(), name='series-detail'),
    
    # URL for adding a new series
    path('series/add/', views.SeriesCreateView.as_view(), name='series-add'),
    
    # URL for updating an existing series
    path('series/<int:pk>/edit/', views.SeriesUpdateView.as_view(), name='series-edit'),
    
    # URL for deleting a series
    path('series/<int:pk>/delete/', views.SeriesDeleteView.as_view(), name='series-delete'),
    
    # URL for listing all questions in a series
    path('questions/', views.QuestionListView.as_view(), name='question-list'),
    
    # URL for viewing a single question
    path('questions/<int:pk>/', views.QuestionDetailView.as_view(), name='question-detail'),
    
    # URL for adding a new question
    path('questions/add/', views.QuestionCreateView.as_view(), name='question-add'),
    
    # URL for updating an existing question
    path('questions/<int:pk>/edit/', views.QuestionUpdateView.as_view(), name='question-edit'),
    
    # URL for deleting a question
    path('questions/<int:pk>/delete/', views.QuestionDeleteView.as_view(), name='question-delete'),

    # URL for viewing the series of a specific category
     path('category/<int:category_id>/series/', views.category_series_view, name='category-series'),

    # URL for viewing the questions of a specific series
    path('series/<int:series_id>/questions/', views.series_questions_view, name='series-questions'),
    
    # URL for tracking student progress
    path('progress/', views.StudentProgressView.as_view(), name='student-progress'),
    
    # URL for submitting an answer
    path('submit-answer/', views.submit_answer, name='submit-answer'),
]
 """

