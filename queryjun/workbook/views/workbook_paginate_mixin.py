from django.core.paginator import Page, Paginator

from ..models import Workbook

class WorkbookPaginateMixin(object):
    def paginate_workbook_fill_dummy(self, page: int, total_per_page: int = 10, latest: bool = False) -> tuple[Page, list[None]]:
        workbooks = Workbook.objects.all().order_by(f"{'-' if latest else ''}id")

        page = Paginator(workbooks, total_per_page).get_page(page)

        return (page, [None] * (total_per_page - len(page.object_list)))
    
    def paginate_workbook(self, page: int, total_per_page: int = 10, latest: bool = False) -> Page:
        return Paginator(Workbook.objects.all().order_by(f"{'-' if latest else ''}id"), total_per_page).get_page(page)