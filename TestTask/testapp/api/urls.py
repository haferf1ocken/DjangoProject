from django.urls import path, include
from testapp import views

urlpatterns = [
    path('deal/create', views.DealCreateView.as_view()),
    path('deals/', views.DealListView.as_view()),
    path('deal/detail/<int:pk>/', views.DealDetailView.as_view()),
]
