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
    async def get(self, request: HttpRequest, *args, **kwargs):
        """
            Returns guess-result page

            :param request:
            :param *args:
            :param **kwargs: 
        """
        guess = await Guess.objects.aget(id=kwargs['guess_id'])
        
        context = {
            'guess': guess,
            'question': await sync_to_async(lambda: guess.question)(),
        }

        task_requesting_mark = asyncio.create_task(self.request_mark(request.user, guess))
        await task_requesting_mark

        return render(request, '../templates/guess_result.html', context)
    
    async def request_mark(self, member: Member, guess: Guess):
        """
            Make a marking request
        """

        # Possible shit storm raiser
        if GuessResult.objects.filter(guess_id=guess.id): return

        database_fetcher = self.determine_vendor(guess)
        comparer = DefaultComparer(guess.question, database_fetcher)

        marking_service = DefaultMarkingService(member, guess, database_fetcher, comparer)
        marking_service.mark()