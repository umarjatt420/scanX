from accounts.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.getUsers_serializer import GetUsersSerializer
from rest_framework import permissions, status

class UpdateUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    @staticmethod
    def patch(request, pk):
        user = User.objects.get(pk=pk)
        serializer = GetUsersSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(data="wrong parameters", status=status.HTTP_400_BAD_REQUEST)
