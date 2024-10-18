from django.core.paginator import Page, Paginator

from ..models import Question

class QuesitionPaginateMixin(object):
    def paginate_question_fill_dummy(self, page: int, total_per_page: int = 10, latest: bool = False) -> tuple[Page, list[None]]:
        questions = Question.objects.all().order_by(f'{'-' if latest else ''}id')

        return Paginator(questions, total_per_page).get_page(page), [None] * (total_per_page - len(questions))

    def paginate_question(self, page: int, total_per_page: int = 10, latest: bool = False) -> Page:
        return Paginator(Question.objects.all().order_by(f'{'-' if latest else ''}id'), total_per_page).get_page(page)