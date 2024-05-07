from django.urls import path

from .views import CommissionDetailView, CommissionListView, CommissionCreateView

urlpatterns = [
    path('list', CommissionListView.as_view(), name = "comList"),
    path('detail/<int:pk>', CommissionDetailView.as_view(), name = "comItem"),
    path('add', CommissionCreateView.as_view(), name = "comAdd"),
]

app_name = "commissions"
