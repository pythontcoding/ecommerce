from django import forms


class ContactForm(forms.Form):

    name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder':'Please enter name'}
        )
    )
    subject = forms.CharField(required=False)
    email_address = forms.EmailField(required=False)
    message = forms.CharField(required=False,widget=forms.Textarea)

    def clean(self):

        clean_data = super(ContactForm, self).clean()

        name = clean_data.get('name')
        subject = clean_data.get('subject')
        email_address = clean_data.get('email_address')
        message = clean_data.get('message')

        if not name:
            raise forms.ValidationError("Name is required can't be blank")
        elif not subject:
            raise forms.ValidationError("Subject is required can't be blank")
        elif not email_address:
            raise forms.ValidationError("Email is required can't be blank")
        elif not message:
            raise forms.ValidationError("Message is required can't be blank")
