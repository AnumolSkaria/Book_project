from django.contrib import admin
from django.urls import path
from Vendor.views import *

urlpatterns = [
    path('home/',getHome,name='home'),

    path('addcategory/',add_category,name='addcategory'),
    path('listcategory/',listCategory,name='listcategory'),
    path('deletecategory/<int:pk>',deleteCategory,name='deletecategory'),
    path('updatecategory/<int:pk>',updateCategory,name='updatecategory'),

    path('createbook/',book_create,name='createbook'),
    path('listbooks/',list_books,name='listbooks'),
    path('viewbook/<int:pk>',viewBook,name='viewbook'),
    path('deletebook/<int:pk>',deleteBook,name='deletebook'),
    path('updatebook/<int:pk>', updateBook, name='updatebook'),

    path('addauthor/',add_author,name='addauthor'),
    path('listauthor/',listAuthor,name='listauthor'),
    path('deleteauthor/<int:pk>',deleteAuthor,name='deleteauthor'),
    path('updateauthor/<int:pk>',updateAuthor,name='updateuthor'),

]