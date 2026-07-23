from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',        include('routes.urls')),
    path('search/', include('schedules.urls')),
    path('book/',   include('bookings.urls')),
    path('users/',  include('users.urls')),
    path('manage/',     include('management.urls')),
]