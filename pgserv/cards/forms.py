from django import forms

class RollsForm(forms.Form):
    username = forms.CharField(max_length=100)

class ClaimForm(forms.Form):
    username = forms.CharField(max_length=100)
    card_id = forms.IntegerField()
