from rest_framework import serializers
from accounts.models import User
class GetUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'is_staff', 'is_active', 'is_superuser']
