from accounts.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status


class DeleteUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def delete(request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_200_OK)
