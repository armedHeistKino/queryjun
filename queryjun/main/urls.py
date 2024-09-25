from django.urls import path

from .views.main_view import MainView

app_name = 'main'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
]