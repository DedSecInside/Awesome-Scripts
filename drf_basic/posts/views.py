from django.shortcuts import render
from .models import post, category
from .serializers import postserializer, categoryserializers
#from django.http import HttpResponse
from rest_framework.views import APIView
#from django.shortcuts import get_object_or_404
from rest_framework.response import Response
#from rest_framework import status
# Create your views here.
class postlist(APIView):

    # def get(self, request):
    #     book1 = post.objects.all()
    #     serializer = postserializer(book1, many=True)
    #     return Response(serializer.data)

    def get(self, request):
        return Response(postserializer(post.objects.all(), many=True).data)

class categorylist(APIView):

    # def get(self, request):
    #     book1 = post.objects.all()
    #     serializer = postserializer(book1, many=True)
    #     return Response(serializer.data)

    def get(self, request):
        return Response(categoryserializers(category.objects.all(), many=True).data)