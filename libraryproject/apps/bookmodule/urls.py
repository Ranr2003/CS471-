from django.urls import path
from . import views
# urlpatterns = [
#     path('', views.index),
#     path('index/<int:val1>/', views.index),
#     path('<int:bookId>', views.viewbook), # هذا الرابط يستقبل أي رقم بعد /books/
# ]
#------------------------------------
urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
]