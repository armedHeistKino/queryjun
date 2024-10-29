from django.urls import path

from .views.notice_detail_view import NoticeDetailView

urlpatterns = [
    path('<int:notice_id>/', NoticeDetailView.as_view(), name='notice-detail'),
]