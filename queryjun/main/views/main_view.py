from django import views
from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render

from ...question.models import Question

class MainView(views.View):
    """
        A CBV for displaying main page
    """
    def _paginate_questions(self, request: HttpRequest) -> Paginator:
        """
            Return a paginator for question list from request

            :param request:
        """
        paginator = Paginator(Question.objects.all().order_by('id'), 10)
        post = paginator.get_page(request.GET.get('page'))

        return post
    
    def get(self, request: HttpRequest, *args, **kwargs):
        """
            Returns main page

            :param request:
            :param *args:
            :param **kwargs:
        """
        context = dict()
        context['member'] = request.user or None

        paginated_posts = self._paginate_questions(request)
        context['questions'] = paginated_posts
        
        return render(request, '../templates/main.html', context)