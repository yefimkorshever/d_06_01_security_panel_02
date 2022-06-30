from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    serialized_non_closed_visits = []
    non_closed_visits = Visit.objects.filter(leaved_at=None)
    visit: Visit
    for visit in non_closed_visits:
        duration = visit.get_duration()
        serialized_non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': localtime(visit.entered_at),
                'duration': visit.format_duration(duration),
                'is_strange': visit.is_long()
            }
        )
    context = {
        'non_closed_visits': serialized_non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
