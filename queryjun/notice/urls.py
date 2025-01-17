from django.urls import path

from .views.notice_list_view import NoticeListView
from .views.notice_detail_view import NoticeDetailView

app_name = 'notice'

urlpatterns = [
    path('', NoticeListView.as_view(), name='notice-list'),
    path('<int:notice_id>/', NoticeDetailView.as_view(), name='notice-detail'),
]