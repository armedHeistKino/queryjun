from django.urls import path

from .views.mark_guess_view import MarkGuessView
from .views.guess_result_view import GuessResultView

app_name = 'mark'

urlpatterns = [
    path('<int:guess_id>/', MarkGuessView.as_view(), name='mark-guess'),
    path('result/<int:guess_id>/', GuessResultView.as_view(), name='guess-result'),
]