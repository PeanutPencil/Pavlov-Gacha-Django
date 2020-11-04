from rest_framework import serializers
from cards.models import Card
from users.serializers import UserSerializer

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['user', 'id', 'name', 'weapon', 'rarity', 'rarity_str', 'image', 'vrml_id',]
    
    user = UserSerializer(read_only=True)
    rarity_str = serializers.SerializerMethodField()

    def get_rarity_str(self, obj):
        if obj.rarity <= 1:
            return 'Banned'
        if obj.rarity <= 4:
            return 'Ultra Rare'
        if obj.rarity <= 9:
            return 'Rare'
        if obj.rarity <= 16:
            return 'Uncommon'
        else:
            return 'Common'
