from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from ..serializers.login_serializer import LoginSerializer
from django.contrib.auth import login
from rest_framework.authtoken.models import Token

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer
    @staticmethod
    def post(request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'success': True,
                'token': token.key,
                             })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
