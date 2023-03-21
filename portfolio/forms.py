from django import forms

class PortfolioSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')