from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserProfileSerializer

from .serializers import UserSerializer
from  rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer

class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()  # Assuming you have a custom user model, replace User with your user model.
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Allow anyone to register

    def perform_create(self, serializer):
        # You can add any additional logic here before saving the user object
        serializer.save()

    


class UserProfileUpdateView(RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
