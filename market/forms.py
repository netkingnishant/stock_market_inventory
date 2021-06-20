from django.forms import ModelForm

from market.models import market


class marketForm(ModelForm):
    class Meta:
        model = market
        fields = ['Name', 'Status', 'Class']
