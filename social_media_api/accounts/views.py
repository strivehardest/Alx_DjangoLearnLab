from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model

from .serializers import RegisterSerializer, LoginSerializer, UserSerializer

User = get_user_model()

# ✅ User Registration
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


# ✅ User Login
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            "token": serializer.validated_data["token"],
            "username": serializer.validated_data["user"].username
        }, status=status.HTTP_200_OK)


# ✅ User Profile (Authenticated)
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
