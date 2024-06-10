from django.urls import path
from .views import upload_file,analyze_data
# from analysis import views



urlpatterns=[
    path('',upload_file,name='upload_file'),
    path('analyze_data/',analyze_data,name='analyze_data'),
]