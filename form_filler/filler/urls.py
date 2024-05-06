from . import views
from django.urls import path


urlpatterns = [
    # path('', views.index, name='index'),
    path('iran/passport/', views.IranPassportCreateView.as_view(), name='filler'), 
    

    
]