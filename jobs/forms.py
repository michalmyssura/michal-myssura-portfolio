from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, label="Imię")
    email = forms.EmailField(required=True, label="Email")
    phone = forms.CharField( max_length=12,required=True,label="Numer Telefonu")
    message = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label="Wiadomość"
    )