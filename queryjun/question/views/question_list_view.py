from django import views
from django.shortcuts import render

from .question_paginate_mixin import QuesitionPaginateMixin

class QuestionListView(QuesitionPaginateMixin, views.View):
    def get(self, request, *args, **kwargs):
        context = {
            'paginated_question': self.paginate_question(page=kwargs['page'], total_per_page=10, latest=True)
        }

        return render(request, '../templates/question_list.html', context)