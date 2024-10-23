from django import views
from django.http import HttpRequest
from django.shortcuts import render

from ...question.models import Question
from ...workbook.models import Workbook

from ...question.views.question_paginate_mixin import QuesitionPaginateMixin
from ...workbook.views.workbook_paginate_mixin import WorkbookPaginateMixin

class MainView(QuesitionPaginateMixin, WorkbookPaginateMixin, views.View):
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
            'paginated_question': self.paginate_question(page=request.GET.get('p', 1), total_per_page=5, latest=True),
            'paginated_workbook': self.paginate_workbook(page=request.GET.get('p', 1), total_per_page=5, latest=False),
        }

        context['statics'] = [
            { 'title': '총 문제 수', 'value': Question.objects.count() },
            { 'title': '총 문제집 수', 'value': Workbook.objects.count() } 
        ]
        
        return render(request, '../templates/main.html', context)