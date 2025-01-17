from django.core.paginator import Page, Paginator

from ..models import Notice

class NoticePaginateMixin(object):
    def paginate_notice_fill_dummy(self, page: int, total_per_page: int = 10, latest: bool = False) -> tuple[Page, list[None]]:
        notices = Notice.objects.all().order_by(f"{'-' if latest else ''}id")

        page = Paginator(notices, total_per_page).get_page(page)

        return (page, [None] * (total_per_page - len(page.object_list)))
    
    def paginate_notice(self, page: int, total_per_page: int = 10, latest: bool = False) -> Page:
        return Paginator(Notice.objects.all().order_by(f"{'-' if latest else ''}id"), total_per_page).get_page(page)