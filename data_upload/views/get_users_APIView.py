from accounts.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.getUsers_serializer import GetUsersSerializer
from rest_framework import permissions, status

class GetUsersView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        users = User.objects.filter(is_superuser=False, is_staff=False, is_active=True)
        serializer = GetUsersSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

