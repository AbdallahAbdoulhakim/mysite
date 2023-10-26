from django.urls import path
from . import views

app_name = "auto"

urlpatterns = [
    path('', views.AutoListView.as_view(), name="auto_list"),
    path('view/<int:pk>/', views.AutoDetailView.as_view(), name="auto_detail"),
    path('create/', views.AutoCreateView.as_view(), name="auto_create"),
    path('update/<int:pk>/', views.AutoUpdateView.as_view(), name="auto_update"),
    path('delete/<int:pk>/', views.AutoDeleteView.as_view(), name="auto_delete"),

    path('make/', views.MakeListView.as_view(), name="make_list"),
    path('make/create/', views.MakeCreateView.as_view(), name="make_create"),
    path('make/view/<int:pk>/', views.MakeDetailView.as_view(), name="make_detail"),
    path('make/update/<int:pk>/', views.MakeUpdateView.as_view(), name="make_update"),
    path('make/delete/<int:pk>/', views.MakeDeleteView.as_view(), name="make_delete"),
]
