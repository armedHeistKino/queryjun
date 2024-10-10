from django.urls import path

from .views.workbook_list_view import WorkbookListView
from .views.workbook_detail_view import WorkbookDetailView

app_name = 'workbook'

urlpatterns = [
    path('', WorkbookListView.as_view(), name='workbook-list'),
    path('<int:workbook_id>/', WorkbookDetailView.as_view(), name='workbook-detail'),
]