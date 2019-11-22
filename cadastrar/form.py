from django.forms import ModelForm
from cadastrar.models import Clientes

class FormClientes(ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'
