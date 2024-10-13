from django import views
from django.core.paginator import Paginator
from django.shortcuts import render

from ..models import Workbook

from .workbook_paginate_mixin import WorkbookPaginateMixin

class WorkbookListView(WorkbookPaginateMixin, views.View):
    def get(self, request, *args, **kwargs):
        """
        
        """
        context = {
            'paginated_workbook': self.paginate_workbook(page=kwargs['page'], total_per_page=10, latest=False)
        }

        return render(request, '../templates/workbook_list.html', context)