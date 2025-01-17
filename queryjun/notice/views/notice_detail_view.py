from django import views
from django.shortcuts import render
from django.http import HttpRequest

from ..models import Notice

class NoticeDetailView(views.View):
    def get(self, request: HttpRequest, *args, **kwargs):
        context = { 
            'notice': Notice.objects.get(id=kwargs['notice_id']) 
        }
        
        return render(request, '../templates/notice_detail.html', context)