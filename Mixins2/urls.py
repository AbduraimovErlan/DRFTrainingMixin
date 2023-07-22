from django.urls import path
from Mixins2 import views



urlpatterns = [
    path('books2/', views.BookListCreateMixins2.as_view()),
    path('books2/<int:pk>/', views.BookRetrieveUpdateDestroyMixins2.as_view()),
]