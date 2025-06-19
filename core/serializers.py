from rest_framework import serializers
from .models import User, Group, Expense, Split

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class SplitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Split
        fields = '__all__'
