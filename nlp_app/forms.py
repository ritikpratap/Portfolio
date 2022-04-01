from django import forms

class MessageForm(forms.Form):

    msg = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'style': 'border-radius: 3%;', 'placeholder':'type...'})
    )