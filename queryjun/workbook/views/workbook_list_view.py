from django import views
from django.core.paginator import Paginator
from django.shortcuts import render

from ..models import Workbook

class WorkbookListView(views.View):
    def get(self, request, *args, **kwargs):
        """
        
        """
        context = {
            'created_workbook': self._pagenate_workbook(request, *args, **kwargs)
        }

        return render(request, '../templates/workbook_list.html', context)
    
    def _pagenate_workbook(self, request, *args, **kwargs) -> Paginator:
        """

        """
        paginator = Paginator(Workbook.objects.all().order_by('id'), 10)
        post = paginator.get_page(request.GET.get('page'))

        return post