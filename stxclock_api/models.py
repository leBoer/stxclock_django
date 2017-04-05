import pytz
from django.db import models
from timezone_field import TimeZoneField
from pygments.lexers import get_lexer_by_name, get_all_lexers
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Exchange(models.Model):
    ticker = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=140)
    location = models.CharField(max_length=140)
    timezone = TimeZoneField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    owner = models.ForeignKey('auth.User', related_name='exchanges', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        """
        Use the 'pygments' library to create a highlighted HTML representation of the code snippet
        """
        options = self.name and {'name': self.name} or {}
        super(Exchange, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Weekend(models.Model):
    exchange = models.ForeignKey(Exchange, related_name='weekend', on_delete=models.CASCADE)
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'
    WEEKEND_CHOICES = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    )
    day = models.CharField(max_length=10, choices=WEEKEND_CHOICES, default=SATURDAY)

    class Meta:
        ordering = ('exchange', 'day',)

    def __str__(self):
        return self.day

class Holiday(models.Model):
    exchange = models.ForeignKey(Exchange, related_name='holidays', on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        ordering = ('exchange', 'date',)

    def __str__(self):
        date = self.date.strftime("%B %d, %Y")
        return  date

