from django.urls import path

from . import views

urlpatterns = [

    path('report_card/', views.report_card),
]