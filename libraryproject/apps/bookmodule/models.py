from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50) # عنوان الكتاب [cite: 96]
    author = models.CharField(max_length=50) # المؤلف [cite: 97]
    price = models.FloatField(default=0.0) # السعر [cite: 97]
    edition = models.SmallIntegerField(default=1) # الطبعة [cite: 98]
