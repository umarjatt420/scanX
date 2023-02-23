from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.login_serializer import LoginSerializer
from django.middleware.csrf import get_token
from django.contrib.auth import login

class LoginView(APIView):
    @staticmethod
    def post(request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            csrf_token = get_token(request)
            login(request, user)
            return Response({
                'success': True,
                'csrf_token': csrf_token
                             })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
