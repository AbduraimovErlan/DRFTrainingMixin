from django.urls import path
from Mixins1 import views


urlpatterns = [
    path('books1/', views.BookListCreateMixins1.as_view()),
    path('books1/<int:pk>/', views.BookRetrieveUpdateDestroyMixins1.as_view())
]