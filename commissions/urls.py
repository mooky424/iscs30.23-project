from django.urls import path
from .views import CommissionListView, CommissionDetailView

urlpatterns = [
    path('list', CommissionListView.as_view(), name = "comList"),
    path('<int:pk>', CommissionDetailView.as_view(), name = "comItem"),
]

app_name = "commissions"