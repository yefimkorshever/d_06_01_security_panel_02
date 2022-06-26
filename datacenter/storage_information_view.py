from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def format_duration(duration):
    days = '' if duration.days == 0 else f'{duration.days}d '
    hours = duration.seconds // 3600
    minutes = duration.seconds % 3600 // 60
    return f'{days}{hours:02}h {minutes:02}m'


def storage_information_view(request):
    non_closed_visits = []
    remaining_visits = Visit.objects.filter(leaved_at=None)
    for visit in remaining_visits:
        duration = visit.get_duration()
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': localtime(visit.entered_at),
                'duration': format_duration(duration)
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
