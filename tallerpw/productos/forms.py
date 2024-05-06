from django import forms
from .models import Cambio_stock

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Cambio_stock

        fields = [
            'ref_id',
            'cantidad',
            'comentario'
        ]

        labels = {
            'ref_id':'Producto',
            'cantidad':'Cantidad',
            'comentario':'Comentario',   
        }

        widgets = {
            'ref_id': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'comentario': forms.TextInput(attrs={'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['ref_id'].error_messages = {'required': 'custom required message'}
        

        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required':'El campo {fieldname} es obligatorio'.format(
                fieldname=field.label)}
       
        