import django_filters as filters

from registration.models import Client


class ClientFilter(filters.FilterSet):
    full_name = filters.CharFilter(field_name='full_name', lookup_expr='icontains')
    passport_seria = filters.CharFilter(field_name='passport_seria', lookup_expr='icontains')
    passport_pinfl = filters.CharFilter(field_name='passport_pinfl', lookup_expr='icontains')
    gender = filters.ChoiceFilter(field_name='gender')

    class Meta:
        model = Client
        fields = ['full_name', 'passport_seria', 'passport_pinfl', 'gender']
