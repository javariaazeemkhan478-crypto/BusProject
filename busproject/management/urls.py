from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Old CRUD pages (keep these)
    path('cities/',                  views.city_list,      name='city_list'),
    path('cities/add/',              views.city_create,    name='city_create'),
    path('cities/edit/<int:pk>/',    views.city_edit,      name='city_edit'),
    path('cities/delete/<int:pk>/',  views.city_delete,    name='city_delete'),
    path('buses/',                   views.bus_list,       name='bus_list'),
    path('buses/add/',               views.bus_create,     name='bus_create'),
    path('buses/edit/<int:pk>/',     views.bus_edit,       name='bus_edit'),
    path('buses/delete/<int:pk>/',   views.bus_delete,     name='bus_delete'),
    path('routes/',                  views.route_list,     name='route_list'),
    path('routes/add/',              views.route_create,   name='route_create'),
    path('routes/edit/<int:pk>/',    views.route_edit,     name='route_edit'),
    path('routes/delete/<int:pk>/',  views.route_delete,   name='route_delete'),
    path('schedules/',               views.schedule_list,  name='schedule_list'),
    path('schedules/add/',           views.schedule_create,name='schedule_create'),
    path('schedules/edit/<int:pk>/', views.schedule_edit,  name='schedule_edit'),
    path('schedules/delete/<int:pk>/',views.schedule_delete,name='schedule_delete'),

    # AJAX endpoints
    path('ajax/<str:section>/',                      views.ajax_list,   name='ajax_list'),
    path('ajax/<str:section>/create/',               views.ajax_create, name='ajax_create'),
    path('ajax/<str:section>/edit/<int:pk>/',        views.ajax_edit,   name='ajax_edit'),
    path('ajax/<str:section>/delete/<int:pk>/',      views.ajax_delete, name='ajax_delete'),
]