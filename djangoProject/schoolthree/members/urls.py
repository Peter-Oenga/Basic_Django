from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path('profile/', views.profile, name="profile"),
    path("profile/details/<int:id>", views.Details, name="Details"),
    path('testing/', views.testing, name="testing")
]