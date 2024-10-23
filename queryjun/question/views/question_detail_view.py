from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import TemplateView

from ..models.question import Question

class QuestionDetailView(TemplateView):
    """
        A CBV for displaying question detail page

        - What if request comes with non-existing question.id number?
        - dirty code -- To be worked...
    """
    template_name = '../templates/question_detail.html'

    def get(self, request: HttpRequest, *args, **kwargs):
        """
            Build question detail page & return question detail page

            :param request:
            :param *args:
            :param **kwargs:
        """
        qid = self.kwargs['question_id']
        
        context = {
            'question': self._get_question(qid),
            'is_solved': self._is_solved(request, qid) if request.user.is_authenticated else False, 
            'submit_forbidden': False,
        }

        return render(request, self.template_name, context)
    
    def _get_question(self, question_id):
        """
            Fetch question an object with given question_id

            :param question_id: Question id to find
        """
        return Question.objects.filter(id=question_id).first()
    
    def _is_solved(self, request: HttpRequest, question_id):
        """
            Check given question is solved

            :param request:
            :param question_id: Question id to determine if it is solved by signed-in member
        """
        try:
            request.user.solved_question.get(id=question_id)
        except Question.DoesNotExist:
            return False
        else:
            return True