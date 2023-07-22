from rest_framework import serializers
from Mixins5.models import Book5



class SerializersBook5(serializers.ModelSerializer):
    class Meta:
        model = Book5
        fields = '__all__'