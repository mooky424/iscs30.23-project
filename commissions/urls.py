from django.urls import path

from .views import (
    CommissionCreateView,
    CommissionDetailView,
    CommissionListView,
    CommissionUpdateView,
)

urlpatterns = [
    path("list", CommissionListView.as_view(), name="comList"),
    path("detail/<int:pk>", CommissionDetailView.as_view(), name="comItem"),
    path("add", CommissionCreateView.as_view(), name="comAdd"),
    path("<int:pk>/edit", CommissionUpdateView.as_view(), name="comEdit"),
]

app_name = "commissions"
