from django import forms

from .models import IranPassport


class IranPassportForm(forms.ModelForm):
    class Meta:
        model = IranPassport
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
