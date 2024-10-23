from django import views
from django.shortcuts import render

from .question_paginate_mixin import QuesitionPaginateMixin

class QuestionListView(QuesitionPaginateMixin, views.View):
    def get(self, request, *args, **kwargs):
        """
        
        """
        questions, empty = self.paginate_question_fill_dummy(page=int(request.GET.get('page', 1)), total_per_page=10, latest=True)

        context = {
            'paginated_question': questions,
            'empty': empty
        }

        return render(request, '../templates/question_list.html', context)