from django import views
from django.http import HttpRequest
from django.shortcuts import render

from ...question.views.question_paginate_mixin import QuesitionPaginateMixin

class MainView(QuesitionPaginateMixin, views.View):
    """
        A CBV for displaying main page
    """
    def get(self, request: HttpRequest, *args, **kwargs):
        """
            Returns main page

            :param request:
            :param *args:
            :param **kwargs:
        """
        context = {
            'member': request.user or None,
            'paginated_question': self.paginate_question(request, 5)
        }
        
        return render(request, '../templates/main.html', context)