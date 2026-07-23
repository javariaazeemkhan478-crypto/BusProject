from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from schedules.models import Schedule
from .models import Booking
@login_required
def book_seat(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    booked_seats = Booking.objects.filter(
        schedule=schedule, status='confirmed'
    ).values_list('seat_number', flat=True)
    all_seats = range(1, schedule.bus.total_seats + 1)

    if request.method == 'POST':
        seat_numbers = request.POST.getlist('seat_number')
        errors = []
        for seat in seat_numbers:
            seat = int(seat)
            if seat in booked_seats:
                errors.append(f'Seat {seat} was already booked!')
            else:
                Booking.objects.create(
                    user=request.user,
                    schedule=schedule,
                    seat_number=seat
                )
        if errors:
            return render(request, 'bookings/book.html', {
                'schedule': schedule,
                'error': ' | '.join(errors),
                'booked_seats': booked_seats,
                'all_seats': all_seats
            })
        return redirect('my_bookings')

    return render(request, 'bookings/book.html', {
        'schedule': schedule,
        'booked_seats': booked_seats,
        'all_seats': all_seats
    })

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booked_at')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    booking.status = 'cancelled'
    booking.save()
    return redirect('my_bookings')