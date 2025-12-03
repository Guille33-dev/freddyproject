from django.db import models


class Party(models.Model):
    # Fiesta asociada a un animatrónico
    name = models.CharField(max_length=100)          # Nombre de la fiesta
    attendants = models.IntegerField()               # Número de asistentes

    def __str__(self):
        return f"{self.name} ({self.attendants} attendants)"


class Animatronic(models.Model):
    # Opciones de tipo de animal (2 caracteres almacenados)
    ANIMAL_CHOICES = [
        ("BE", "Bear"),
        ("CH", "Chicken"),
        ("BU", "Bunny"),
        ("FO", "Fox"),
    ]

    # Nombre del animatrónico (obligatorio, máx 50 caracteres)
    name = models.CharField(max_length=50)

    # Tipo de animal, representado como select
    animal = models.CharField(max_length=2, choices=ANIMAL_CHOICES)

    # Fecha de construcción como texto (máx 20); el formulario usará widget de fecha
    build_date = models.CharField(max_length=20)

    # Indica si está retirado (obligatorio)
    decommissioned = models.BooleanField()

    # Fiestas asociadas al animatrónico (no obligatorio)
    parties = models.ManyToManyField(Party, blank=True)

    def __str__(self):
        return self.name
