from django.forms import ModelForm
from Vendor.models import *

class BookCreator(ModelForm):
    class Meta:
        model=Book
        fields=["book_name","category_name","author_name","price","pages","pub_date"]

    def clean(self):
        print("inside clean")

class AuthorCreator(ModelForm):
    class Meta:
        model=Author
        fields=["author_name"]

        def clean(self):
            print("inside clean")
            cleaned_data=super().clean()
            name=cleaned_data.get("author_name")
            ob=Author.objects.get(author_name=name)
            if(ob):
                self.add_error("author_name","This author is already exists")
class CategoryCreator(ModelForm):
    class Meta:
        model=Category
        fields=["category_name"]

        def clean(self):
            print("inside clean")

class UpdateBook(ModelForm):
    class Meta:
        model=Book
        fields="__all__"

        def clean(self):
            pass
class UpdateAuthor(ModelForm):
    class Meta:
        model=Author
        fields="__all__"

        def clean(self):
            pass
class UpdateCategory(ModelForm):
    class Meta:
        model=Category
        fields="__all__"

        def clean(self):
            pass