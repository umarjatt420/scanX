from rest_framework import serializers
from accounts.models import User
class GetUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'is_superuser', 'is_staff', 'is_active']
