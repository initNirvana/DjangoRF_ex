from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # __all__ 로 해도 됨, 혹은 exclude[id]
        fields = ['bid', 'title','author','category','pages','price','published_date', 'description']
    