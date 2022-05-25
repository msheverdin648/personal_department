from django.urls import path

from . import views

urlpatterns = [
    path('', views.DocumentsView.as_view(), name='documents'),
    path('add/', views.DocumetnsAdd.as_view(), name='add'),
    path('change/<int:pk>/', views.DocumentsChange.as_view(), name='change'),
    path('delete/<int:pk>/', views.DocumentsDelete.as_view(), name='delete'),
    path('filter/', views.DocumentsFilter.as_view(), name='filter'),


]