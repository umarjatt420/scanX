from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

class GetUserEmailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        user = request.user
        return Response({
            'email': user.email,
            'is_superuser': user.is_superuser
        }, status=status.HTTP_200_OK)
