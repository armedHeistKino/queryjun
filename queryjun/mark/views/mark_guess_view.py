from django import views
from django.http import HttpRequest
from django.shortcuts import redirect, resolve_url, render
from asgiref.sync import sync_to_async

from ...member.models import Member

from ...submit.models import Guess
from .marking_service import DefaultMarkingService
from .database_fetcher import DatabaseFetcher, PostgresqlFetcher

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
        await self._request_mark(request.user, Guess.objects.get(id=kwargs['guess_id']), PostgresqlFetcher())

        context = {
            'guess_id': guess.id,
            'guess': guess, 
            'question': guess.question,
        }

        return await sync_to_async(render)(request, '../templates/guess_result.html', context)
    
    async def _request_mark(self, member: Member, guess: Guess, db_fetcher: DatabaseFetcher):
        marking_service = DefaultMarkingService(member, guess, db_fetcher)
        marking_service.mark()