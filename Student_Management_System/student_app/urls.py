from django.urls import path
from .views import ( add_student , view_student , update_student , delete_student )

urlpatterns = [
    path('add/',add_student,name='add_student'),
    path('view/',view_student,name='view_student'),
    path('update/<int:pk>/',update_student,name='update_student'),
    path('delete/<int:pk>/',delete_student,name='delete_student')
]