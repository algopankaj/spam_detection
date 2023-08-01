from django.shortcuts import render

# Create your views here.
# api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, PhoneNumberSpam
from .serializers import UserSerializer

class UserRegistration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhoneNumberSpamView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        if phone_number:
            try:
                phone_number_spam = PhoneNumberSpam.objects.get(phone_number=phone_number)
                phone_number_spam.spam_likelihood += 1
                phone_number_spam.save()
            except PhoneNumberSpam.DoesNotExist:
                PhoneNumberSpam.objects.create(phone_number=phone_number, spam_likelihood=1)
            return Response({'message': 'Phone number marked as spam.'}, status=status.HTTP_200_OK)
        return Response({'error': 'Phone number is required.'}, status=status.HTTP_400_BAD_REQUEST)

class SearchUserView(APIView):
    def get(self, request):
        search_query = request.query_params.get('q')
        if search_query:
            users = User.objects.filter(name__icontains=search_query).order_by('-name')
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'Search query parameter "q" is required.'}, status=status.HTTP_400_BAD_REQUEST)
