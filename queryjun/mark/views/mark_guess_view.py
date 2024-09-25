from django import views
from django.http import HttpRequest
from django.shortcuts import redirect, resolve_url

from ...submit.models import Guess
from ..models import ResultType

from .database_fetcher import PostgresqlFetcher
from .marking import Marking

class MarkGuessView(views.View):
    """
        A CBV for marking gussed query and displaying guess result page
    """
    def get(self, request: HttpRequest, *args, **kwargs):
        """
            Returns guess-result page

            :param request:
            :param *args:
            :param **kwargs: 
        """
        guess = Guess.objects.get(id=kwargs['guess_id'])
        guess_result = Marking(guess, PostgresqlFetcher()).mark()

        if guess_result.result == ResultType.objects.filter(result_acronym='CLR').first():
            request.user.solved_question.add(guess.question)

        return redirect(resolve_url('mark:guess-result', guess_result_id=guess_result.id))