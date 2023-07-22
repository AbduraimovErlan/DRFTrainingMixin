from django.urls import path
from Mixins3 import views


urlpatterns = [
    path('books3/', views.BookListCreateAPIView3.as_view()),
    path('books3/<int:pk>/', views.BookRetrieveUpdateDestroyAPIView3.as_view()),
]