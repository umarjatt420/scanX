from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import logout

class LogoutView(APIView):
    @staticmethod
    def get(request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
