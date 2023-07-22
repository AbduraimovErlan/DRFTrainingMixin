from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from Mixins2.models import Book2
from Mixins2.serializers import SerializersBook2




class BookListCreateMixins2(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Book2.objects.all()
    serializer_class = SerializersBook2


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BookRetrieveUpdateDestroyMixins2(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Book2.objects.all()
    serializer_class = SerializersBook2
    lookup_field = 'pk'



    def get(self, reqeust, *args, **kwargs):
        return self.retrieve(reqeust, *args, **kwargs)

    def put(self, reqeust, *args, **kwargs):
        return self.update(reqeust, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)