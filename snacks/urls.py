from django.urls import path
from .views import SnackListView, SnackDetailview

urlpatterns = [
    path('', SnackListView.as_view(), name='snack_list'),
    path('snack/<int:pk>/', SnackDetailview.as_view(), name='snack_detail'),
]