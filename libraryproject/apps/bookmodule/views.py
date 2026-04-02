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
#-----------------------------------------------
def links_view(request):
    return render(request, 'bookmodule/links.html')
def formatting_view(request):
    return render(request, 'bookmodule/formatting.html')
def listing_view(request):
    return render(request, 'bookmodule/listing.html')
def tables_view(request):
    return render(request, 'bookmodule/tables.html')
#----------------------------------------------- لاب6
from django.shortcuts import render

def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]
# الداله قبل التحديث
# def search(request):
#     return render(request, 'bookmodule/search.html')

# الخطوة الخامسة: معالجة نموذج البحث (Logic Handling)
# الآن سنقوم بتعديل دالة search التي كتبناها سابقاً لتقوم بالآتي:
#
# التأكد ما إذا كان المستخدم قد ضغط على زر البحث (أي أن الطلب من نوع POST).
#
# استلام الكلمة المفتاحية (Keyword) والخيارات (Title/Author).
#
# تصفية (Filter) قائمة الكتب بناءً على مدخلات المستخدم.
def search(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword').lower()  # جلب الكلمة وتحويلها لصغير
        isTitle = request.POST.get('option1')  # هل اختار البحث في العنوان؟
        isAuthor = request.POST.get('option2')  # هل اختار البحث في الكاتب؟

        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False

            if isTitle and keyword in item['title'].lower():
                contained = True

            if not contained and isAuthor and keyword in item['author'].lower():
                contained = True

            if contained:
                newBooks.append(item)


        return render(request, 'bookmodule/bookList.html', {'books': newBooks})


    return render(request, 'bookmodule/search.html')
#-----------------------------------------------------------------لاب 7
from .models import Book


def add_test_data(request):
    # إضافة كتاب باستخدام constructor [cite: 116, 117]
    book1 = Book(title='Continuous Delivery', author='J.Humble and D. Farley', price=120.0, edition=3)
    book1.save()  # حفظ الكتاب [cite: 121]

    # إضافة كتاب آخر باستخدام create [cite: 119, 120]
    Book.objects.create(title='Reversing: Secrets of Reverse Engineering', author='E. Eilam', price=97.0, edition=2)

    Book.objects.create(title='The Hundred-Page Machine Learning Book', author='Andriy Burkov', price=100.0, edition=4)

    return render(request, 'bookmodule/index.html')  # اعد توجيهك لأي صفحة بعد الإضافة

def simple_query(request):
    #   هنا انا غيرته عشان ابي تطلع لي نتيجه البحث عن الكتب التي يحتوي عنوانها على 'and' (غير حساس لحالة الأحرف)
    mybooks = Book.objects.filter(title__icontains='Delivery')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')