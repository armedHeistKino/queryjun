from django import views
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

from ..models import GuessResult

from .marking_service import DefaultMarkingService
from .database_fetcher import PostgresqlFetcher
from ...submit.models import Guess

class GuessResultView(views.View):
    """
        A CBV for displaying guess result page
    """
    def get(self, request: HttpRequest, *args, **kwargs):
        """
            Returns guess result page

            :param request:
            :param *args:
            :param **kwargs:
        """

        guess_result = GuessResult.objects.get(guess_id=self.kwargs['guess_id'])

        context = {
            'total_execution_time': guess_result.total_execution_time,
            'result': {
                'result_acronym': guess_result.result.result_acronym
            }
        }

        return JsonResponse(data=context)