from rest_framework import serializers
from cards.models import Card
from users.serializers import UserSerializer

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['user', 'id', 'name', 'weapon', 'rarity', 'image', 'vrml_id',]
    
    user = UserSerializer(read_only=True)

