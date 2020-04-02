from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['pk','first_name', 'last_name', 'email', 'phone','address','description']


