from django.urls import path, include

from .views.question_list_view import QuestionListView
from .views.question_detail_view import QuestionDetailView
from .views.submit_redirect import submit_redirect

app_name = 'question'

urlpatterns = [
    path('list/', QuestionListView.as_view(), name='question-list'), 
    path('<int:question_id>/', QuestionDetailView.as_view(), name='question-detail'),
    path('submit-redirect/<int:question_id>/', submit_redirect, name='submit-redirect'),
]