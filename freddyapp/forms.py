from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Animatronic, Party


class AnimatronicForm(forms.ModelForm):
    # Campo name con mensajes de error personalizados
    name = forms.CharField(
        label="Name",
        max_length=50,
        error_messages={
            "max_length": "The name of the animatronic must not be more than 50 characters long",
            "required": "The name of the animatronic is required",
        },
    )

    # Campo animal como select con opciones del modelo
    animal = forms.ChoiceField(
        label="Animal type",
        choices=Animatronic.ANIMAL_CHOICES,
        required=True,
    )

    # build_date con widget de calendario (input type="date")
    build_date = forms.CharField(
        label="Build date",
        max_length=20,
        widget=forms.DateInput(attrs={"type": "date"}),
        error_messages={
            "required": "The build date is required",
        },
    )

    # Campo booleano obligatorio
    decommissioned = forms.BooleanField(
        label="Decommissioned",
        required=True,
    )

    # Selección múltiple de fiestas; no obligatoria
    parties = forms.ModelMultipleChoiceField(
        label="Parties",
        queryset=Party.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Animatronic
        fields = ["name", "animal", "build_date", "decommissioned", "parties"]


class RegisterForm(UserCreationForm):
    # Formulario sencillo de registro de usuario
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
