from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        end_date = localtime(self.leaved_at) if self.leaved_at else localtime()
        entered_at = localtime(self.entered_at)
        return end_date - entered_at

    def is_long(self, minutes=60):
        duration = self.get_duration()
        return duration.total_seconds() > minutes * 60

    @staticmethod
    def format_duration(duration):
        days = '' if duration.days == 0 else f'{duration.days}d '
        hours = duration.seconds // 3600
        minutes = duration.seconds % 3600 // 60
        return f'{days}{hours:02}h {minutes:02}m'
