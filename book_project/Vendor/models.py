from django.db import models

# Create your models here.

# category model for storing category names

class Category(models.Model):
    category_name=models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.category_name

#  author model for storing author names

class Author(models.Model):
    author_name=models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.author_name


#     book model for book details

class Book(models.Model):
    book_name=models.CharField(max_length=200)
    category_name=models.ForeignKey(Category,on_delete=models.CASCADE)
    author_name=models.ForeignKey(Author,on_delete=models.CASCADE)
    price=models.IntegerField(default=50)
    pages=models.IntegerField(default=60)
    # date=models.DateField(auto_now=True)
    pub_date=models.DateField()


    def __str__(self):
        return self.book_name

