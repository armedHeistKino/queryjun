from django.contrib import admin
from django.urls import path, include

from .views.submit_guess_view import SubmitGuessView

urlpatterns = [
    path('<int:question_id>/', SubmitGuessView.as_view(), name='submit-guess'),
]
