from django.urls import path
from .views import *


app_name = "panel"
urlpatterns = [
    # path('management/',Management.as_view(),name='management'),
    path('ProjectDetail/<int:id>/',ProjectDetail.as_view(),name='ProjectDetail'),
]
