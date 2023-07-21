from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django import utils
from datacenter.duration_calculations import format_duration, get_duration, is_visit_long


def storage_information_view(request):
    non_closed_visits = []
    for visit in Visit.objects.filter(leaved_at=None):
        duration = get_duration(visit.entered_at, visit.leaved_at)
        entered_time = format_duration(visit.entered_at)
        is_strange = is_visit_long(duration)
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': entered_time,
                'duration': duration,
                'is_strange': is_strange
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
