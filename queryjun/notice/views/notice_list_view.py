from django import views
from django.shortcuts import render
from django.http import HttpRequest

from ..models import Notice

from .notice_paginate_mixin import NoticePaginateMixin

class NoticeListView(NoticePaginateMixin, views.View):
    def get(self, request: HttpRequest, *args, **kwargs):
        """

        """
        notices, empty = self.paginate_notice_fill_dummy(page=int(request.GET.get('p', 1)), total_per_page=10, latest=False)
        
        context = {
            'paginated_notice': notices,
            'empty': empty,
        }

        return render(request, '../templates/notice_list.html', context)