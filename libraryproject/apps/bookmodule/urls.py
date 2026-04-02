from django.urls import path
from . import views
# urlpatterns = [
#     path('', views.index),
#     path('index/<int:val1>/', views.index),
#     path('<int:bookId>', views.viewbook), # هذا الرابط يستقبل أي رقم بعد /books/
# ]
#------------------------------------
urlpatterns = [
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links', views.links_view),
    path('html5/text/formatting', views.formatting_view),
    path('html5/listing', views.listing_view),
    path('html5/tables', views.tables_view),
    path('search', views.search, name="search"),#لاب6
    path('add-books/', views.add_test_data),#لاب7
    path('simple/query', views.simple_query),#لاب7 بيظهر نتيجه
    path('complex/query', views.complex_query),#لاب7 لايظهر نتيجه
]