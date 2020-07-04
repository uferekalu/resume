from django import forms


# class Contact_Form(forms.Form):
#     name= forms.CharField(max_length=500, label="Name")
#     email= forms.EmailField(max_length=500, label="Email")
#     comment= forms.CharField(label='',widget=forms.Textarea(
#                         attrs={'placeholder': 'Enter your comment here'}))

class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        print(email)
        return email