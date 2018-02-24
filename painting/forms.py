from django import forms

from painting.models import Painting


class PaintingForm(forms.ModelForm):
    class Meta:
        model = Painting
        exclude = ('id', 'owner')
