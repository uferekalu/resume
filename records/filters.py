import django_filters

from .models import Details

class DetailsFilter(django_filters.FilterSet):
    class Meta:
        model = Details
        fields = '__all__'
        exclude = ['email', 'date_created']