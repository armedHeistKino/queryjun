from django import views
from django.http import HttpRequest
from django.shortcuts import render
from asgiref.sync import sync_to_async

from ...member.models import Member
from ...submit.models import Guess

from .marking_service import DefaultMarkingService
from .database_fetcher import DatabaseFetcher, PostgresqlFetcher
from .comparer import DefaultComparer

class MarkGuessView(views.View):
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
        await self.request_mark(request.user, Guess.objects.get(id=kwargs['guess_id']))

        context = {
            'guess_id': guess.id,
            'guess': guess, 
            'question': guess.question,
        }

        return await sync_to_async(render)(request, '../templates/guess_result.html', context)
    
    async def request_mark(self, member: Member, guess: Guess):
        """
            Make a marking request
        """
        database_fetcher = PostgresqlFetcher(guess)
        comparer = DefaultComparer(guess.question, database_fetcher)

        marking_service = DefaultMarkingService(member, guess, database_fetcher, comparer)
        marking_service.mark()