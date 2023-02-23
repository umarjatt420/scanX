from accounts.models import User
from ..serializers.register_serializer import RegisterSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

# Create your views here.


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
