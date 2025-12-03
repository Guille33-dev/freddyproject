from django.contrib import admin
from .models import Animatronic, Party


@admin.register(Animatronic)
class AnimatronicAdmin(admin.ModelAdmin):
    list_display = ("name", "animal", "build_date", "decommissioned")


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ("name", "attendants")
