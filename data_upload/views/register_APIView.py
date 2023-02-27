from ..serializers.register_serializer import RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions


# Create your views here.
class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    @staticmethod
    def post(request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
