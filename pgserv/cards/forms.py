from django import forms

class RollsForm(forms.Form):
    user_id = forms.IntegerField()

class ClaimForm(forms.Form):
    user_id = forms.IntegerField()
    card_id = forms.IntegerField()

class CardsListForm(forms.Form):
    q = forms.CharField(max_length=16, required=False)
