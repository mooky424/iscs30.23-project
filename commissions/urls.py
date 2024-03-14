from django.urls import path
from .views import commissions_list, commission

urlpatterns = [
    path('commissions/list', commissions_list, name = "comList"),
    path('commissions/<int:pk>', commission, name = "comItem"),
]
