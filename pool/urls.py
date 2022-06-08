from django.urls import path
from . import views


app_name = 'pool'
urlpatterns = [
    path('upload/', views.UploadImageView.as_view(), name='upload_image'),
    path('delete/<int:pk>/', views.DeleteObjectView.as_view(), name='delete_object'),
]
