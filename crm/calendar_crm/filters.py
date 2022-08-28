from django_filters.rest_framework import DateFromToRangeFilter, FilterSet, DateRangeFilter
from tasks.models import Task
class CalendarFilter(FilterSet):
    CHOICES =  [
        ('today', ('Today')),
        ('yesterday', ('Yesterday')),
        ('week', ('Past 7 days')),
        ('month', ('This month')),
        ('year', ('This year')),
    ]

    date = DateFromToRangeFilter()
    
    date_range = DateRangeFilter(field_name='date',choices=CHOICES)
    class Meta:
        
        model = Task
        fields = ['date']