from django.contrib import admin
from django.urls import path

urlpatterns = [
    paht('', include('ledger.urls'), namespace=""),
    path('admin/', admin.site.urls),
]
