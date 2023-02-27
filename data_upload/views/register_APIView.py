from accounts.models import User
from ..serializers.register_serializer import RegisterSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


# class RegisterView(CreateAPIView):
#     queryset = User.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class = RegisterSerializer

class RegisterView(APIView):
    @staticmethod
    def post(request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success': True,
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
