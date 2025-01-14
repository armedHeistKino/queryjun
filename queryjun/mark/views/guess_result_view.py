from django import views
from django.http import HttpRequest, JsonResponse

from ..models import ResultType
from ..models import GuessResult
from ..models import GuessResultError

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
        guess_result = GuessResult.objects.get(guess_id=kwargs['guess_id'])

        context = dict()
        
        if guess_result.result.result_acronym == ResultType.objects.get(result_acronym='ERR').result_acronym:
            error = GuessResultError.objects.get(guess_result_id=guess_result.id)

            context['exception_message'] = error.exception_message

        context['total_execution_time'] = guess_result.total_execution_time
        context['result'] = { 'result_acronym': guess_result.result.result_acronym }

        return JsonResponse(data=context)