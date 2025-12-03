from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

from .forms import AnimatronicForm, RegisterForm
from .models import Animatronic


# Lista de animatrónicos, accesible por cualquier usuario
def animatronic_list(request):
    animatronics = Animatronic.objects.all()
    return render(request, "freddyapp/animatronic_list.html", {"animatronics": animatronics})


# Detalle de un animatrónico, solo usuarios autenticados
@login_required
def animatronic_view(request, id):
    anim = get_object_or_404(Animatronic, pk=id)
    return render(request, "freddyapp/animatronic_detail.html", {"anim": anim})


# Creación de animatrónico, requiere permiso add_animatronic
@permission_required("freddyapp.add_animatronic", raise_exception=True)
def animatronic_new(request):
    if request.method == "POST":
        form = AnimatronicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("animatronic_list")
    else:
        form = AnimatronicForm()
    return render(request, "freddyapp/animatronic_form.html", {"form": form})


# Actualización de animatrónico con vista genérica
class AnimatronicUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Animatronic
    form_class = AnimatronicForm
    template_name = "freddyapp/animatronic_form.html"
    permission_required = "freddyapp.change_animatronic"
    success_url = reverse_lazy("animatronic_list")


# Borrado de animatrónico con vista genérica
class AnimatronicDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Animatronic
    template_name = "freddyapp/animatronic_confirm_delete.html"
    permission_required = "freddyapp.delete_animatronic"
    success_url = reverse_lazy("animatronic_list")


# Registro de usuario; añade por defecto al grupo Client
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            client_group, _ = Group.objects.get_or_create(name="Client")
            user.groups.add(client_group)
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "freddyapp/register.html", {"form": form})


# Login y logout usando las vistas genéricas de Django
class FreddyLoginView(LoginView):
    template_name = "freddyapp/login.html"


class FreddyLogoutView(LogoutView):
    pass


# Establece el tema oscuro mediante cookie
def set_theme_dark(request):
    response = redirect("animatronic_list")
    response.set_cookie("theme", "dark")
    return response


# Borra la cookie de tema
def clear_cookies(request):
    response = redirect("animatronic_list")
    response.delete_cookie("theme")
    return response
