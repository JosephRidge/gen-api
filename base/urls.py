from django.urls import path
from . import views

urlpatterns = [
    path('api/receive-generator-data/', views.receive_generator_data, name='receive_generator_data'),
    path('api/generator-data-csv/', views.generator_data_csv, name='generator_data_csv'),
    path('api/latest-generator-data/', views.get_latest_generator_data, name='get_latest_generator_data'),
] 