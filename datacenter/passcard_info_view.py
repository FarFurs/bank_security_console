from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from datacenter.duration_calculations import format_duration, get_duration, is_visit_long


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = get_object_or_404(Passcard, passcode=passcode)
    for visit in Visit.objects.filter(passcard=passcard):
        entered_at = format_duration(visit.entered_at)
        duration = get_duration(visit.entered_at, visit.leaved_at)
        is_strange = is_visit_long(duration)
        this_passcard_visits.append(
            {
                'entered_at': entered_at,
                'duration': duration,
                'is_strange': is_strange
            },
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
