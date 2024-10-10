from django import views

from django.shortcuts import render

from ..models import Workbook
from ...question.models import Question

class WorkbookDetailView(views.View):
    def get(self, request, *args, **kwargs):
        workbook = Workbook.objects.get(id=kwargs['workbook_id'])

        included_question = workbook.included_question.filter(id=kwargs['workbook_id'])

        context = {
            'workbook': {
                'title': workbook.title,
                'explaination': workbook.explaination,
                'included_question': included_question
            }
        }

        return render(request, '../templates/workbook_detail.html', context)