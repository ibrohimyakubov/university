from django.urls import path
# from .views import HelloWorld
from .views import books_list, book_detail, book_create

urlpatterns = [
    # path('', HelloWorld.as_view()),
    path('', books_list, name='books'),
    path('book_detail/<int:pk>/', book_detail, name='book_detail'),
    path('books/create', book_create, name='book_create')
]