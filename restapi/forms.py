from django import forms
from .models import Place


class PlaceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['lat'].widget.attrs['class'] = 'form-control'
        self.fields['longi'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Place
        fields = "__all__"
