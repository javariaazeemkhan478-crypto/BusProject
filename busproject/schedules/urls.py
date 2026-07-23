from django.urls import path

from schedules.views import search, schedule_detail

urlpatterns = [
    path('', search, name='search'),
    path('<int:pk>/', schedule_detail, name='schedule_detail'),
]