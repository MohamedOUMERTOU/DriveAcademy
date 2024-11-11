# courses/serializers.py

from rest_framework import serializers
from .models import Category, Series, Question, StudentProgress




class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'type', 'image_data', 'audio_data', 'video_data', 'options', 'true_options']
# Serializer for Series
class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ['id', 'name', 'description', 'category']


# Serializer for StudentProgress
class StudentProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProgress
        fields = ['id', 'student', 'question', 'answer', 'date_submitted']
