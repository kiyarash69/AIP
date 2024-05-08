from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label='Name')
    email = forms.EmailField(label='Email')
    title = forms.CharField(max_length=100, label='Title')
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5}),
        label='Description'
    )

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise forms.ValidationError("Description should be at least 10 characters long.")
        return description

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        if not name and not email:
            raise forms.ValidationError("You must provide either a name or an email.")
        return cleaned_data

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=50, label='Name')
#     email = forms.EmailField(label='Email')
#     title = forms.CharField(max_length=100, label='Title')
#     description = forms.CharField(max_length=500)
