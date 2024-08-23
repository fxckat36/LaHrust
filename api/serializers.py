from rest_framework import serializers
from api.models import menu, feedback


class menu_serializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = ['id', 'name', 'cost', 'about', 'path']

class feedback_serializer(serializers.ModelSerializer):
    class Meta:
        model = feedback
        fields = ['name', 'comment', 'rate']