from django import views
from django.http import Http404, HttpRequest
from django.shortcuts import render

from ...member.models import Member
from ...mark.models import GuessResult

from .specific_member_mixin import SpecificMemberMixin

class GuessHistoryView(SpecificMemberMixin, views.View):
    """
        A CBV for displaying guess history page
    """
    def get(self, request: HttpRequest, *args, **kwargs):
        """
            Returns guess history page

            :param request:
            :param *args:
            :param **kwargs:
        """
        try:
            member = self.get_specific_member(request, *args, **kwargs)
        except Member.DoesNotExist:
            raise Http404('Member does not exist.')

        guesses = GuessResult.objects \
                .select_related('guess') \
                .filter(guess__submitter=member) \
                .order_by('-guess__id')

        context = {
            'member': member,
            'guess_result': guesses, 
        }

        return render(request, '../templates/guess_history.html', context)