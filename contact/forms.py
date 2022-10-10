from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'query', 'message',)

    # def __init__(self, *args, **kwargs):
    #     """ Add classes to form fields """
    #     super().__init(*args, **kwargs)

    #     for field in self.fields:
    #         self.fields[field].widget.attrs['class'] = 'border-dark rounded-0 '
