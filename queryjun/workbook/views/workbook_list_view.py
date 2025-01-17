from django import views
from django.shortcuts import render

from ...workbook.models import Workbook

from .workbook_paginate_mixin import WorkbookPaginateMixin

class WorkbookListView(WorkbookPaginateMixin, views.View):
    def get(self, request, *args, **kwargs):
        """
        
        """
        workbook, empty = self.paginate_workbook_fill_dummy(page=int(request.GET.get('p', 1)), total_per_page=10, latest=False)

        context = {
            'paginated_workbook': workbook,
            'empty': empty,
        }

        return render(request, '../templates/workbook_list.html', context)