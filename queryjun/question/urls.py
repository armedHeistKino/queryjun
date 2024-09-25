from django.urls import path, include

from .views.question_detail_view import QuestionDetailView
from .views.submit_redirect import submit_redirect

app_name = 'question'

urlpatterns = [
    path('<int:question_id>/', QuestionDetailView.as_view(), name='question-detail'),
    path('submit-redirect/<int:question_id>/', submit_redirect, name='submit-redirect'),
]