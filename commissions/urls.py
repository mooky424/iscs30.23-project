from django.urls import path

from .views import CommissionDetailView, CommissionListView, CommissionCreateView, CommissionUpdateView, JobApplicationCreateView

urlpatterns = [
    path('list', CommissionListView.as_view(), name = "comList"),
    path('detail/<int:pk>', CommissionDetailView.as_view(), name = "comItem"),
    path('add', CommissionCreateView.as_view(), name = "comAdd"),
    path('<int:pk>/update', CommissionUpdateView.as_view(), name = "comUpdate"),
    path('<int:pk>/signup', JobApplicationCreateView.as_view(), name = "comApp"),
]

app_name = "commissions"
