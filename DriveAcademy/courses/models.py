from django.db import models
from django.contrib.auth.models import User  # Assuming you are using Django's built-in User model



class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Series(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Question(models.Model):
    type = models.CharField(max_length=10, choices=[('image', 'Image'), ('video', 'Video')])
    image_data = models.BinaryField(blank=True, null=True)
    audio_data = models.BinaryField(blank=True, null=True)
    video_data = models.BinaryField(blank=True, null=True)
    options = models.JSONField()
    true_options = models.JSONField()

    def __str__(self):
        return f"Question {self.id}"


class SeriesQuestion(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    class Meta:
        unique_together = ('series', 'question')

    def __str__(self):
        return f"{self.series.title} - Question {self.question.id} (Order {self.order})"


class StudentProgress(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.JSONField()  # Stores the student's selected answers
    is_correct = models.BooleanField()  # Tracks whether the answer was correct or not
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'series', 'question')

    def __str__(self):
        return f"{self.student.user.username} - {self.series.title} - Question {self.question.id}"


class SeriesCompletion(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    completion_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.user.username} - {self.series.title} (Completed: {self.is_completed})"
