from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from cards.models import Card
from cards.serializers import CardSerializer
from django.http import Http404
import random
from cards.forms import RollsForm, ClaimForm, CardsListForm
from users.models import User


class CardList(APIView):
    """ List all cards or create a new card """
    def get(self, request):
        form = CardsListForm(request.query_params)
        if not form.is_valid():
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
        q = form.cleaned_data["q"]
        if q :
            cards = Card.objects.filter(name__icontains=q)
        else:
            cards = Card.objects.all()        
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     

class CardDetail(APIView):
    """
    Retrieve, update or delete a card instance.
    """
    def get_object(self, pk):
        try:
            return Card.objects.get(pk=pk)
        except Card.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        card = self.get_object(pk)
        serializer = CardSerializer(card)
        return Response(serializer.data)

    def put(self, request, pk):
        card = self.get_object(pk)
        serializer = CardSerializer(card, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        card = self.get_object(pk)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RollView(APIView):
    """ return random unclaimed card """
    def post(self, request):
        # form validation 
        form = RollsForm(request.data)
        if not form.is_valid():
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
        # verifying user can roll
        user = User.objects.get(pk=form.cleaned_data["user_id"])
        if user.rolls <= 0 :
            return Response("user does not have enough rolls", status=status.HTTP_400_BAD_REQUEST)
        # getting the card
        cards = Card.objects.filter(user=None)
        card = random.choice(cards)
        serializer = CardSerializer(card)
        # reducing rolls
        user.rolls -= 1
        user.save()
        
        return Response(serializer.data)
    
class ClaimView(APIView):
    def post(self, request):
        # form validation 
        form = ClaimForm(request.data)
        if not form.is_valid():
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
        # verifying user can claim
        user = User.objects.get(pk=form.cleaned_data["user_id"])
        if user.claims <= 0 :
            return Response("user does not have enough claims", status=status.HTTP_400_BAD_REQUEST)
        # getting the card
        card = Card.objects.get(pk = form.cleaned_data["card_id"])
        # assign the user to the card
        card.user = user
        card.save()
        serializer = CardSerializer(card)
        # reducing claims
        user.claims -= 1
        user.save()
        return Response(serializer.data)