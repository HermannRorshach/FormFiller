from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'iran/passport/',
        views.IranPassportCreateView.as_view(),
        name='filler'),
]
