# courses/views.py

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Category, Series, Question, StudentProgress
from .serializers import SeriesSerializer, QuestionSerializer, StudentProgressSerializer
from rest_framework.parsers import MultiPartParser, FormParser



 # ViewSet for Series
class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

    # Custom action to get questions in a specific series
    @action(detail=True, methods=['get'])
    def questions(self, request, pk=None):
        series = self.get_object()
        questions = series.questions.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data) 
# ViewSet for Question
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# ViewSet for Student Progress
class StudentProgressViewSet(viewsets.ModelViewSet):
    queryset = StudentProgress.objects.all()
    serializer_class = StudentProgressSerializer

    # Custom action to get the progress of a specific student
    @action(detail=False, methods=['get'])
    def progress_by_student(self, request):
        student = request.user
        progress = StudentProgress.objects.filter(student=student)
        serializer = StudentProgressSerializer(progress, many=True)
        return Response(serializer.data)
