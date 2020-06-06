from django import forms


class searchForm(forms.Form):
    searchkey = forms.CharField(max_length=100)