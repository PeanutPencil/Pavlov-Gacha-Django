from rest_framework import serializers
from users.models import User
#from cards.serializers import CardSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'rolls', 'claims', 'avatar_url'] #cards
    #cards = CardSerializer(many=True, read_only=True)
