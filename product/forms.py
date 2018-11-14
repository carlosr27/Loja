from django.forms import ModelForm, TextInput

from product.models import Color


class ColorForm(ModelForm):
    class Meta:
        model = Color
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color'})
        }
