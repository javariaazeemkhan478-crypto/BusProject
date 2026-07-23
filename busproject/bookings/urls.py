from django.urls import path
from . import views

urlpatterns = [
    path('<int:schedule_id>/',       views.book_seat,       name='book_seat'),
    path('my/',                      views.my_bookings,     name='my_bookings'),
    path('cancel/<int:booking_id>/', views.cancel_booking,  name='cancel_booking'),
]