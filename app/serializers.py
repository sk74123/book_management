from rest_framework import serializers
from app.models import Borrow_book

class Borrow_book_serializer(serializers.ModelSerializer):
    class Meta:
        model= Borrow_book
        fields= ('__all__')