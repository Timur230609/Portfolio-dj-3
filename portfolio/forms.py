from django.forms import ModelForm
from .models import Contact
from django import forms

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["your_name",  "your_email", "subject", "massage" ]
    
    def clean(self):
        super(ContactForm, self).clean()
        
    
        your_name = self.cleaned_data.get('your_name')
        content = self.cleaned_data.get('content')

      
        if your_name:
            if len(your_name) < 3:
                raise forms.ValidationError("your_name must be at least 3 characters")
        else:
            self._errors['your_name'] = self.error_class([
                    'your_name is required'])

        if not content:
            self._errors['content'] = self.error_class([
                    'Content is required'])
        
        return self.cleaned_data
