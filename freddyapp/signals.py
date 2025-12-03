from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from .models import Animatronic


# Crea o actualiza los grupos Client y Staff con los permisos requeridos
def create_groups_and_permissions(sender, **kwargs):
    content_type = ContentType.objects.get_for_model(Animatronic)

    # Todos los permisos asociados al modelo Animatronic
    all_perms = Permission.objects.filter(content_type=content_type)

    # Grupo Staff: todos los permisos del modelo Animatronic
    staff_group, _ = Group.objects.get_or_create(name="Staff")
    staff_group.permissions.set(all_perms)

    # Grupo Client: solo permiso de ver Animatronic
    client_group, _ = Group.objects.get_or_create(name="Client")
    view_perm = Permission.objects.get(
        content_type=content_type, codename="view_animatronic"
    )
    client_group.permissions.set([view_perm])
