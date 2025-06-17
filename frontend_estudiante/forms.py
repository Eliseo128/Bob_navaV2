from django  import forms
from . models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ["num_estudiante", "nombre", "apellido", "email", "area_estudio", "gpa"]
        labels = {
            'num_estudiante': 'Número de Estudiante',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo Electrónico',
            'area_estudio': 'Área de Estudio',
            'gpa': 'GPA',
        }
        widgets = {
            'num_estudiante': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'area_estudio': forms.TextInput(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }


