from django.urls import path
from .views import CommissionListView, CommissionDetailView

urlpatterns = [
    path('commissions/list', CommissionListView.as_view(), name = "comList"),
    path('commissions/<int:pk>', CommissionDetailView.as_view(), name = "comItem"),
]

app_name = "commissions"