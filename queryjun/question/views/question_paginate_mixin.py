from django.core.paginator import Page, Paginator

from ..models import Question

class QuesitionPaginateMixin(object):
    def paginate_question(self, page: int, total_per_page: int = 10, latest: bool = False) -> Page:
        return Paginator(Question.objects.all().order_by(f'{'-' if latest else ''}id'), total_per_page).get_page(page)