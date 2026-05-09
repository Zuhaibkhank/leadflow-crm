from django.urls import path

from .views import (
    lead_list,
    add_lead,
    edit_lead,
    delete_lead
)

app_name = "leads"

urlpatterns = [

    path("", lead_list, name="list"),

    path("add/", add_lead, name="add"),

    path("edit/<int:pk>/", edit_lead, name="edit"),

    path("delete/<int:pk>/", delete_lead, name="delete"),

]