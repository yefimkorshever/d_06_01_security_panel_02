from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.models import Passcard, Visit


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)
    serialized_passcard_visits = []
    visit: Visit
    for visit in passcard_visits:
        duration = visit.get_duration()
        serialized_passcard_visits.append(
            {
                'entered_at': localtime(visit.entered_at),
                'duration': visit.format_duration(duration),
                'is_strange': visit.is_long()
            }
        )

    context = {
        'passcard': passcard,
        'this_passcard_visits': serialized_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
