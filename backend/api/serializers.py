from rest_framework import serializers
from .models import FindClosingBracket


class FindClosingBracketSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindClosingBracket
        fields = '__all__'
