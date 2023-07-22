from django.urls import path
from Mixins5 import views


urlpatterns = [
    path('books5/', views.BookListCreateAPIView5.as_view()),
    path('books5/<int:pk>/', views.BookRetrieveUpdateDestroyAPIView5.as_view()),
]