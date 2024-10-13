from django.core.paginator import Page, Paginator

from ..models import Question

class QuesitionPaginateMixin(object):
    def paginate_question(self, page: int, total_per_page: int = 10) -> Page:
        return Paginator(Question.objects.all().order_by('id'), total_per_page).get_page(page)
