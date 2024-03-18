from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    
    # هذا الجزء خاص بعمل حالة ان البوست في المسوده او تم الموافقة علي نشره
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    
    # هذا الجزء خاص بعمل ترتيب للبوستات من الاحدث للاقدم بناء علي تاريخ النشر
    class Meta:
        ordering = ['-publish']
        # هذا ال انديكس تقوم بتحسين عملية جلب البيانات من قاعدة البيانات
        indexes = [
            models.Index(fields=['-publish']),
        ]
    # هذا الجزء خاص بعرض البوست بدلا من عرض اسمه ال اي دي سوف يتم عرضه باسمه في لوحة تحكم الادمن
    def __str__(self):
        return self.title
