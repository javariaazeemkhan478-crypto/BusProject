from django.shortcuts import render, get_object_or_404
from .models import Schedule

def search(request):
    results = []
    from_city = request.GET.get('from_city')
    to_city   = request.GET.get('to_city')
    date      = request.GET.get('date')

    if from_city and to_city and date:
        results = Schedule.objects.filter(
            route__from_city__name=from_city,
            route__to_city__name=to_city,
            departure_time__date=date
        )
    return render(request, 'schedules/search.html', {
        'results': results,
        'from_city': from_city,
        'to_city': to_city,
        'date': date
    })

def schedule_detail(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    return render(request, 'schedules/detail.html', {'schedule': schedule})