from .models import StudentProgress, SeriesQuestion, SeriesCompletion
from django.db.models import Count

def calculate_accuracy(student, series):
    """
    Calculate the accuracy of a student in a given series.
    """
    total_questions = SeriesQuestion.objects.filter(series=series).count()
    correct_answers = StudentProgress.objects.filter(
        student=student,
        series=series,
        is_correct=True
    ).count()
    if total_questions > 0:
        accuracy = (correct_answers / total_questions) * 100
        return accuracy
    return 0


def mark_series_as_completed(student, series):
    """
    Marks a series as completed if the student has answered all questions correctly.
    """
    completed_questions = StudentProgress.objects.filter(
        student=student,
        series=series,
        is_correct=True
    ).count()
    total_questions = SeriesQuestion.objects.filter(series=series).count()
    
    if completed_questions == total_questions:
        # Mark series as completed
        SeriesCompletion.objects.update_or_create(
            student=student,
            series=series,
            defaults={'is_completed': True}
        )
        return True  # Indicating that the series has been completed
    return False  # If not all questions are answered correctly


def track_answer_submission(student, series, question, selected_option):
    """
    Track student's answer submission for a given question in a series.
    It also calculates whether the answer is correct and updates the progress.
    """
    # Check if the answer is correct
    question_instance = question
    correct_answers = question_instance.true_options
    
    is_correct = set(selected_option) == set(correct_answers)
    
    # Record the answer submission
    student_progress, created = StudentProgress.objects.update_or_create(
        student=student,
        series=series,
        question=question,
        defaults={'selected_option': selected_option, 'is_correct': is_correct}
    )
    
    # Update series completion status after each submission
    if mark_series_as_completed(student, series):
        return True  # The series has been completed
    return False  # The series is still in progress


def get_student_progress(student, series):
    """
    Get the student's progress (number of correct answers) in a given series.
    """
    correct_answers = StudentProgress.objects.filter(
        student=student,
        series=series,
        is_correct=True
    ).count()
    
    total_questions = SeriesQuestion.objects.filter(series=series).count()
    
    return {
        'correct_answers': correct_answers,
        'total_questions': total_questions,
        'accuracy': calculate_accuracy(student, series)
    }
