from django.urls import path

from . import views


app_name = 'filler'

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'iran/passport/',
        views.IranPassportCreateView.as_view(),
        name='filler'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('upload-sample', views.UploadSample.as_view(), name='upload_sample')
]
