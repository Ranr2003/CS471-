# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse("Hello, world!")
#-----------------------------------------
# from django.http import HttpResponse
#
# def index(request):
#     # الحصول على قيمة الاسم من الرابط، وإذا لم يوجد نستخدم "world!" كافتراضي
#     name = request.GET.get("name") or "world!"
#     return HttpResponse("Hello, " + name)   # try in braeser  : http://127.0.0.1:8000/?name=Otarr
# def index2(request, val1=0):
#     return HttpResponse("value1 = " + str(val1)) # try in brawser : http://127.0.0.1:8000/index2/5/

#-----------------------------------------
from django.shortcuts import render

# def index(request):
#     return render(request, 'bookmodule/index2.html')
# def index(request):
#     name = request.GET.get("name") or "world!"
#     return render(request, 'bookmodule/index2.html', {"name": name})
#
# #إضافة دالة عرض الكتاب (View)
# def viewbook(request, bookId):
#     # بيانات تجريبية لمحاكاة قاعدة البيانات [cite: 175]
#     book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
#     book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
#
#     targetBook = None
#     if book1['id'] == bookId: targetBook = book1
#     if book2['id'] == bookId: targetBook = book2
#
#     context = {'book': targetBook}  # نمرر الكتاب للقالب [cite: 182]
#     return render(request, 'bookmodule/show.html', context)
#-------------------------------------------------
def index(request):
    return render(request, "bookmodule/index.html")
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')