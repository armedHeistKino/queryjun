from django import views
from django.http import HttpRequest
from django.shortcuts import render

from ...member.models import Member
from ...submit.models import Guess

from .marking_service import DefaultMarkingService
from .fetcher_vendor_determiner_mixin import FetcherVendorDeterminerMixin
from .comparer import DefaultComparer

class MarkGuessView(FetcherVendorDeterminerMixin, views.View):
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
        self.request_mark(request.user, guess)

        context = {
            'guess': guess,
            'question': guess.question,
        }

        return render(request, '../templates/guess_result.html', context)
    
    def request_mark(self, member: Member, guess: Guess):
        """
            Make a marking request
        """
        database_fetcher = self.determine_vendor(guess)

        comparer = DefaultComparer(guess.question, database_fetcher)
        marking_service = DefaultMarkingService(member, guess, database_fetcher, comparer)

        marking_service.mark()