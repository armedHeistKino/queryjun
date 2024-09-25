from django import views
from django.http import HttpRequest
from django.shortcuts import render

from ..models import GuessResult

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
        result = GuessResult.objects.filter(id=kwargs['guess_result_id']).first()
        
        context = {
            'guess': result.guess,
            'guess_result': result,
            'question': result.guess.question
        }

        return render(request, '../templates/guess_result.html', context)