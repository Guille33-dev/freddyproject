from django.apps import AppConfig


class FreddyappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "freddyapp"

    # Conectamos la señal que creará grupos y permisos
    def ready(self):
        from django.db.models.signals import post_migrate
        from .signals import create_groups_and_permissions

        post_migrate.connect(create_groups_and_permissions, sender=self)
