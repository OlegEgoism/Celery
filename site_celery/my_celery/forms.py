from django import forms


class InfoForm(forms.Form):
    name = forms.CharField(max_length=250)
    number_1 = forms.IntegerField()
    number_2 = forms.IntegerField()
