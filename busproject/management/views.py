from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from routes.models import City, Route
from buses.models import Bus
from schedules.models import Schedule

# ─── DASHBOARD ────────────────────────────────────────
@staff_member_required
def dashboard(request):
    return render(request, 'management/dashboard.html', {
        'city_count':     City.objects.count(),
        'route_count':    Route.objects.count(),
        'bus_count':      Bus.objects.count(),
        'schedule_count': Schedule.objects.count(),
    })

# ─── CITIES ───────────────────────────────────────────
@staff_member_required
def city_list(request):
    cities = City.objects.all()
    return render(request, 'management/city_list.html', {'cities': cities})

@staff_member_required
def city_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            City.objects.create(name=name)
            return redirect('city_list')
    return render(request, 'management/city_form.html', {'action': 'Add'})

@staff_member_required
def city_edit(request, pk):
    city = get_object_or_404(City, pk=pk)
    if request.method == 'POST':
        city.name = request.POST.get('name')
        city.save()
        return redirect('city_list')
    return render(request, 'management/city_form.html', {'action': 'Edit', 'obj': city})

@staff_member_required
def city_delete(request, pk):
    city = get_object_or_404(City, pk=pk)
    if request.method == 'POST':
        city.delete()
        return redirect('city_list')
    return render(request, 'management/confirm_delete.html', {'obj': city, 'type': 'City'})

# ─── BUSES ────────────────────────────────────────────
@staff_member_required
def bus_list(request):
    buses = Bus.objects.all()
    return render(request, 'management/bus_list.html', {'buses': buses})

@staff_member_required
def bus_create(request):
    if request.method == 'POST':
        Bus.objects.create(
            bus_number  = request.POST.get('bus_number'),
            total_seats = request.POST.get('total_seats'),
            bus_type    = request.POST.get('bus_type'),
        )
        return redirect('bus_list')
    return render(request, 'management/bus_form.html', {'action': 'Add'})

@staff_member_required
def bus_edit(request, pk):
    bus = get_object_or_404(Bus, pk=pk)
    if request.method == 'POST':
        bus.bus_number  = request.POST.get('bus_number')
        bus.total_seats = request.POST.get('total_seats')
        bus.bus_type    = request.POST.get('bus_type')
        bus.save()
        return redirect('bus_list')
    return render(request, 'management/bus_form.html', {'action': 'Edit', 'obj': bus})

@staff_member_required
def bus_delete(request, pk):
    bus = get_object_or_404(Bus, pk=pk)
    if request.method == 'POST':
        bus.delete()
        return redirect('bus_list')
    return render(request, 'management/confirm_delete.html', {'obj': bus, 'type': 'Bus'})

# ─── ROUTES ───────────────────────────────────────────
@staff_member_required
def route_list(request):
    routes = Route.objects.all()
    return render(request, 'management/route_list.html', {'routes': routes})

@staff_member_required
def route_create(request):
    cities = City.objects.all()
    if request.method == 'POST':
        Route.objects.create(
            from_city_id  = request.POST.get('from_city'),
            to_city_id    = request.POST.get('to_city'),
            distance_km   = request.POST.get('distance_km'),
        )
        return redirect('route_list')
    return render(request, 'management/route_form.html', {'action': 'Add', 'cities': cities})

@staff_member_required
def route_edit(request, pk):
    route  = get_object_or_404(Route, pk=pk)
    cities = City.objects.all()
    if request.method == 'POST':
        route.from_city_id = request.POST.get('from_city')
        route.to_city_id   = request.POST.get('to_city')
        route.distance_km  = request.POST.get('distance_km')
        route.save()
        return redirect('route_list')
    return render(request, 'management/route_form.html', {'action': 'Edit', 'obj': route, 'cities': cities})

@staff_member_required
def route_delete(request, pk):
    route = get_object_or_404(Route, pk=pk)
    if request.method == 'POST':
        route.delete()
        return redirect('route_list')
    return render(request, 'management/confirm_delete.html', {'obj': route, 'type': 'Route'})

# ─── SCHEDULES ────────────────────────────────────────
@staff_member_required
def schedule_list(request):
    schedules = Schedule.objects.all()
    return render(request, 'management/schedule_list.html', {'schedules': schedules})

@staff_member_required
def schedule_create(request):
    routes = Route.objects.all()
    buses  = Bus.objects.all()
    if request.method == 'POST':
        Schedule.objects.create(
            route_id       = request.POST.get('route'),
            bus_id         = request.POST.get('bus'),
            departure_time = request.POST.get('departure_time'),
            arrival_time   = request.POST.get('arrival_time'),
            fare           = request.POST.get('fare'),
        )
        return redirect('schedule_list')
    return render(request, 'management/schedule_form.html', {
        'action': 'Add', 'routes': routes, 'buses': buses
    })

@staff_member_required
def schedule_edit(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    routes   = Route.objects.all()
    buses    = Bus.objects.all()
    if request.method == 'POST':
        schedule.route_id       = request.POST.get('route')
        schedule.bus_id         = request.POST.get('bus')
        schedule.departure_time = request.POST.get('departure_time')
        schedule.arrival_time   = request.POST.get('arrival_time')
        schedule.fare           = request.POST.get('fare')
        schedule.save()
        return redirect('schedule_list')
    return render(request, 'management/schedule_form.html', {
        'action': 'Edit', 'obj': schedule, 'routes': routes, 'buses': buses
    })

@staff_member_required
def schedule_delete(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == 'POST':
        schedule.delete()
        return redirect('schedule_list')
    return render(request, 'management/confirm_delete.html', {'obj': schedule, 'type': 'Schedule'})


import json
from django.http import JsonResponse

def ajax_list(request, section):
    if section == 'cities':
        items = list(City.objects.values('id', 'name'))
        return JsonResponse({'items': items, 'count': len(items)})

    elif section == 'buses':
        items = list(Bus.objects.values('id', 'bus_number', 'bus_type', 'total_seats'))
        return JsonResponse({'items': items, 'count': len(items)})

    elif section == 'routes':
        routes = Route.objects.select_related('from_city', 'to_city').all()
        items = [{
            'id':          r.id,
            'from_city':   r.from_city.name,
            'to_city':     r.to_city.name,
            'from_city_id': r.from_city_id,
            'to_city_id':  r.to_city_id,
            'distance_km': r.distance_km
        } for r in routes]
        return JsonResponse({'items': items, 'count': len(items)})

    elif section == 'schedules':
        schedules = Schedule.objects.select_related('route', 'bus').all()
        items = [{
            'id':               s.id,
            'route':            str(s.route),
            'route_id':         s.route_id,
            'bus':              s.bus.bus_number,
            'bus_id':           s.bus_id,
            'departure_time':   s.departure_time.strftime('%d %b %Y, %H:%M'),
            'departure_time_raw': s.departure_time.strftime('%Y-%m-%dT%H:%M'),
            'arrival_time_raw': s.arrival_time.strftime('%Y-%m-%dT%H:%M'),
            'fare':             str(s.fare),
        } for s in schedules]
        return JsonResponse({'items': items, 'count': len(items)})

    return JsonResponse({'error': 'Invalid section'}, status=400)


def ajax_create(request, section):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    data = json.loads(request.body)
    try:
        if section == 'cities':
            City.objects.create(name=data['name'])
        elif section == 'buses':
            Bus.objects.create(
                bus_number=data['bus_number'],
                total_seats=data['total_seats'],
                bus_type=data['bus_type']
            )
        elif section == 'routes':
            Route.objects.create(
                from_city_id=data['from_city'],
                to_city_id=data['to_city'],
                distance_km=data['distance_km']
            )
        elif section == 'schedules':
            Schedule.objects.create(
                route_id=data['route'],
                bus_id=data['bus'],
                departure_time=data['departure_time'],
                arrival_time=data['arrival_time'],
                fare=data['fare']
            )
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


def ajax_edit(request, section, pk):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    data = json.loads(request.body)
    try:
        if section == 'cities':
            obj = get_object_or_404(City, pk=pk)
            obj.name = data['name']
            obj.save()
        elif section == 'buses':
            obj = get_object_or_404(Bus, pk=pk)
            obj.bus_number  = data['bus_number']
            obj.total_seats = data['total_seats']
            obj.bus_type    = data['bus_type']
            obj.save()
        elif section == 'routes':
            obj = get_object_or_404(Route, pk=pk)
            obj.from_city_id = data['from_city']
            obj.to_city_id   = data['to_city']
            obj.distance_km  = data['distance_km']
            obj.save()
        elif section == 'schedules':
            obj = get_object_or_404(Schedule, pk=pk)
            obj.route_id       = data['route']
            obj.bus_id         = data['bus']
            obj.departure_time = data['departure_time']
            obj.arrival_time   = data['arrival_time']
            obj.fare           = data['fare']
            obj.save()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


def ajax_delete(request, section, pk):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    try:
        if section == 'cities':
            get_object_or_404(City, pk=pk).delete()
        elif section == 'buses':
            get_object_or_404(Bus, pk=pk).delete()
        elif section == 'routes':
            get_object_or_404(Route, pk=pk).delete()
        elif section == 'schedules':
            get_object_or_404(Schedule, pk=pk).delete()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})