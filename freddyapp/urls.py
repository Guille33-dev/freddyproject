from django.urls import path

from . import views

urlpatterns = [
    path("list", views.animatronic_list, name="animatronic_list"),
    path("new", views.animatronic_new, name="animatronic_new"),
    path("<int:id>/view", views.animatronic_view, name="animatronic_view"),
    path("<int:pk>/edit", views.AnimatronicUpdate.as_view(), name="animatronic_edit"),
    path("<int:pk>/delete", views.AnimatronicDelete.as_view(), name="animatronic_delete"),
    path("newuser", views.register, name="register"),
    path("login", views.FreddyLoginView.as_view(), name="login"),
    path("logout", views.FreddyLogoutView.as_view(), name="logout"),
    path("theme", views.set_theme_dark, name="set_theme_dark"),
    path("clearcookies", views.clear_cookies, name="clear_cookies"),
]
