import django_filters
from .models import EventList

class EventFilter(django_filters.FilterSet):

    CHOICES= (
        ('ascending','ASCENDING'),
        ('descending','DESCENDING')
    )
    ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_order')

    class Meta:
        model= EventList

        fields = ['category','price','country']

    def filter_by_order(self, queryset, name, value):
        expression = 'created' if value == 'ascending' else '-created'
        return queryset.order_by(expression)