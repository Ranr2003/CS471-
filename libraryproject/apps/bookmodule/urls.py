from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('index/<int:val1>/', views.index),
    path('<int:bookId>', views.viewbook), # هذا الرابط يستقبل أي رقم بعد /books/
]