from django.db import models

class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('issued', 'Issued'),
    ]
   
    title = models.CharField(max_length=200, db_index=True)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    publication_year = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    added_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title