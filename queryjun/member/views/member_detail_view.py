from django.http import Http404, HttpRequest
from django.views.generic import TemplateView
from django.shortcuts import render

from ..models import Member
from .specific_member_mixin import SpecificMemberMixin

class MemberDetailView(SpecificMemberMixin, TemplateView):
    """
        A CBV for displaying member detail page
    """
    template_name = "../templates/member_detail.html"

    def get(self, request: HttpRequest, *args, **kwargs):
        """
            Returns member detail page

            :param request:
            :param *args:
            :param **kwargs:
        """
        try:
            member = self.get_specific_member(request, *args, **kwargs)
        except Member.DoesNotExist:
            raise Http404('Member does not exist.')
        
        solved_question = member.solved_question.all()
        context = { 
            'member': member, 
            'solved_question': solved_question 
        }

        return render(request, '../templates/member_detail.html', context)